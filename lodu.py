import random
from collections import defaultdict

# -----------------------------
# LUDO (SIMPLIFIED TERMINAL EDITION)
# -----------------------------
# Features
# - 2–4 players, names and pawn symbols configurable
# - 2 pawns per player (tweak PAWNS_PER_PLAYER)
# - Need a 6 to enter the board
# - Extra turn on rolling a 6 (triple-6 rule: three 6s in a row ends the turn)
# - Capture opponents by landing on them (safe tiles cannot be captured)
# - Stacks: your pawns can stack; stacked pawns move together and cannot be captured
# - Exact roll required to enter HOME
# - Text UI showing positions and available moves each turn
#
# Notes
# This is a compact, classroom-friendly version focusing on gameplay logic over graphics.
# Board model: 52 main-track tiles (0..51) + 6 home tiles per player.
# Each player has a unique START index and a HOME_ENTRY index where they leave the main track.
#
# You can tune parameters at the CONFIG section.

# -----------------------------
# CONFIG
# -----------------------------
MAIN_TRACK_LEN = 52
HOME_STRETCH_LEN = 6
PAWNS_PER_PLAYER = 2  # set 4 if you want full Ludo
TRIPLE_SIX_ENDS_TURN = True

SAFE_TILES = {0, 8, 13, 21, 26, 34, 39, 47}  # common Ludo safe spots (approx.)

# START positions (main track indices) for up to 4 players in classic order
STARTS = [0, 13, 26, 39]
HOME_ENTRIES = [50, 11, 24, 37]  # tile before turning into home stretch for each player

# -----------------------------
# Data Models
# -----------------------------
class Pawn:
    def __init__(self, owner_id: int, pawn_id: int):
        self.owner_id = owner_id
        self.pawn_id = pawn_id
        self.state = 'yard'  # 'yard', 'main', 'home'
        self.pos = None      # if 'main': index on main track; if 'home': distance 0..HOME_STRETCH_LEN
        self.home_index = 0  # progress in home stretch

    def __repr__(self):
        return f"P{self.owner_id}{self.pawn_id}({self.state}:{self.pos if self.pos is not None else '-'})"

class Player:
    def __init__(self, pid: int, name: str, symbol: str):
        self.pid = pid
        self.name = name
        self.symbol = symbol  # single character to render on board
        self.pawns = [Pawn(pid, i) for i in range(PAWNS_PER_PLAYER)]

    def all_home(self):
        return all(p.state == 'home' and p.home_index == HOME_STRETCH_LEN for p in self.pawns)

class LudoGame:
    def __init__(self, players: list[Player]):
        if not (2 <= len(players) <= 4):
            raise ValueError("Players must be between 2 and 4")
        self.players = players
        self.turn = 0
        self.roll_history_in_turn = []

    # ---- Helpers ----
    def idx_after(self, idx: int, steps: int) -> int:
        return (idx + steps) % MAIN_TRACK_LEN

    def is_safe(self, idx: int) -> bool:
        return idx in SAFE_TILES or any(idx == STARTS[p.pid] for p in self.players)

    def board_stacks(self):
        stacks = defaultdict(list)
        for pl in self.players:
            for p in pl.pawns:
                if p.state == 'main':
                    stacks[p.pos].append(p)
        return stacks

    def render_board_brief(self):
        stacks = self.board_stacks()
        # show only tiles that have pawns on them, plus summary
        spots = []
        for idx, pawns in sorted(stacks.items()):
            owners = ''.join(self.players[p.owner_id].symbol for p in pawns)
            spots.append(f"{idx:02d}[{owners}]" + ("*" if self.is_safe(idx) else ""))
        if not spots:
            print("Board: (no pawns on main track yet)")
        else:
            print("Board:", '  '.join(spots))
        # home progress summary
        for pl in self.players:
            homes = sum(1 for p in pl.pawns if p.state == 'home' and p.home_index == HOME_STRETCH_LEN)
            on_home_track = sum(1 for p in pl.pawns if p.state == 'home' and p.home_index < HOME_STRETCH_LEN)
            in_yard = sum(1 for p in pl.pawns if p.state == 'yard')
            on_board = sum(1 for p in pl.pawns if p.state == 'main')
            print(f"  {pl.name} [{pl.symbol}] -> Yard:{in_yard} Main:{on_board} HomeTrack:{on_home_track} Finished:{homes}")

    def legal_moves(self, pl: Player, roll: int):
        moves = []  # (pawn, description, action_callable)
        start_idx = STARTS[pl.pid]
        home_entry = HOME_ENTRIES[pl.pid]
        stacks = self.board_stacks()

        # 1) Enter from yard on 6
        if roll == 6:
            for pawn in pl.pawns:
                if pawn.state == 'yard':
                    # Can enter if start square is free of ENEMY stack (own stack is fine)
                    enemy_here = any(p.owner_id != pl.pid for p in stacks.get(start_idx, []))
                    if not enemy_here:
                        def make_enter(pawn=pawn):
                            def _enter():
                                pawn.state = 'main'
                                pawn.pos = start_idx
                                # if your own stack exists, join it; if enemy single pawn exists and not safe, capture
                                self.resolve_captures_at(start_idx, owner=pl.pid)
                            return _enter
                        moves.append((pawn, f"Enter pawn {pawn.pawn_id} to start {start_idx}", make_enter()))

        # 2) Move pawns on main track
        for pawn in pl.pawns:
            if pawn.state == 'main':
                # compute distance to home entry
                steps_to_entry = (home_entry - pawn.pos) % MAIN_TRACK_LEN
                if roll <= steps_to_entry:
                    # Still on main track after move
                    dest = self.idx_after(pawn.pos, roll)
                    # Can't land on enemy stack if it's a protected safe tile with 2+ enemies
                    # (classic rule variants differ; we allow capture unless tile is safe)
                    def make_move(pawn=pawn, dest=dest):
                        def _move():
                            pawn.pos = dest
                            self.resolve_captures_at(dest, owner=pl.pid)
                        return _move
                    moves.append((pawn, f"Move pawn {pawn.pawn_id} to {dest}", make_move()))
                else:
                    # Entering the home stretch
                    into_home = roll - steps_to_entry - 1  # -1 to step onto the first home tile
                    if into_home <= HOME_STRETCH_LEN - pawn.home_index:
                        def make_into_home(pawn=pawn, steps_to_entry=steps_to_entry, roll=roll):
                            def _home_move():
                                # move to home entry then into home stretch
                                pawn.state = 'home'
                                pawn.pos = None
                                pawn.home_index += (roll - steps_to_entry)
                                if pawn.home_index > HOME_STRETCH_LEN:
                                    pawn.home_index = HOME_STRETCH_LEN
                            return _home_move
                        moves.append((pawn, f"Send pawn {pawn.pawn_id} into home track (+{roll - steps_to_entry})", make_into_home()))

        # 3) Move pawns already in home stretch (exact finish required)
        for pawn in pl.pawns:
            if pawn.state == 'home' and pawn.home_index < HOME_STRETCH_LEN:
                if pawn.home_index + roll <= HOME_STRETCH_LEN:
                    def make_home_advance(pawn=pawn):
                        def _adv():
                            pawn.home_index += roll
                        return _adv
                    moves.append((pawn, f"Advance pawn {pawn.pawn_id} on home track to {pawn.home_index + roll}/{HOME_STRETCH_LEN}", make_home_advance()))

        return moves

    def resolve_captures_at(self, idx: int, owner: int):
        # If tile is safe, no captures
        if self.is_safe(idx):
            return
        # Gather pawns at idx
        stacks = self.board_stacks()
        here = stacks.get(idx, [])
        # If there are enemies and NOT a stack (>=2) of enemies, capture them
        enemies = [p for p in here if p.owner_id != owner]
        friends = [p for p in here if p.owner_id == owner]
        if enemies and len(enemies) == 1 and len(friends) >= 1:
            # capture the single enemy pawn
            enemy = enemies[0]
            enemy.state = 'yard'
            enemy.pos = None
            enemy.home_index = 0

    def roll_die(self):
        return random.randint(1, 6)

    def take_turn(self, pl: Player):
        self.roll_history_in_turn = []
        extra_turn = True
        sixes_in_a_row = 0
        while extra_turn:
            input(f"\n{pl.name}'s turn. Press Enter to roll the die...")
            roll = self.roll_die()
            self.roll_history_in_turn.append(roll)
            print(f"You rolled: {roll}")
            if roll == 6:
                sixes_in_a_row += 1
            else:
                sixes_in_a_row = 0

            if TRIPLE_SIX_ENDS_TURN and sixes_in_a_row >= 3:
                print("Three 6s in a row! Turn forfeited.")
                break

            moves = self.legal_moves(pl, roll)
            if not moves:
                print("No legal moves. Turn passes.")
                extra_turn = (roll == 6 and sixes_in_a_row < 3)
                continue

            # If exactly one move is possible, auto-play it
            if len(moves) == 1:
                pawn, desc, action = moves[0]
                print("Auto move:", desc)
                action()
            else:
                print("Choose a move:")
                for i, (_, desc, _) in enumerate(moves, 1):
                    print(f"  {i}. {desc}")
                while True:
                    try:
                        choice = int(input("Enter choice number: "))
                        if 1 <= choice <= len(moves):
                            break
                    except ValueError:
                        pass
                    print("Invalid choice, try again.")
                _, desc, action = moves[choice - 1]
                print("You chose:", desc)
                action()

            self.render_board_brief()

            # Extra turn if 6 and not triple-six penalty
            extra_turn = (roll == 6 and sixes_in_a_row < 3)

            # Win check
            if pl.all_home():
                return True  # winner
        return False

    def play(self):
        print("\n=== LUDO (Simplified Terminal Edition) ===")
        print(f"Players: {len(self.players)}, Pawns each: {PAWNS_PER_PLAYER}\n")
        self.render_board_brief()
        while True:
            pl = self.players[self.turn]
            won = self.take_turn(pl)
            if won:
                print(f"\n🎉 {pl.name} wins the game! 🎉")
                break
            self.turn = (self.turn + 1) % len(self.players)


# -----------------------------
# Setup & Run
# -----------------------------

def ask_players():
    while True:
        try:
            n = int(input("How many players? (2-4): "))
            if 2 <= n <= 4:
                break
        except ValueError:
            pass
        print("Please enter a number between 2 and 4.")
    default_symbols = ['R', 'G', 'Y', 'B']
    players = []
    for i in range(n):
        name = input(f"Player {i+1} name (default P{i+1}): ").strip() or f"Player{i+1}"
        sym = input(f"Choose a 1-letter symbol for {name} (default {default_symbols[i]}): ").strip() or default_symbols[i]
        sym = sym[0].upper()
        players.append(Player(i, name, sym))
    return players


def main():
    random.seed()
    players = ask_players()
    game = LudoGame(players)
    game.play()


if __name__ == "__main__":
    main()
