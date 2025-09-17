#!/usr/bin/env python3
"""
Quiz Game Show - Full featured console version

Features:
- Timer per question (Easy/Medium/Hard -> different time limits)
- Lifelines per player: 50/50, Ask the Audience, Skip (one use each)
- Randomized question order and randomized option order
- Multiple players (turn-based)
- Difficulty selection
- Save high scores to highscores.json
- Exactly 10 questions per game
"""

import random
import json
import os
import sys
import threading
import queue
from datetime import datetime

HIGHSCORE_FILE = "highscores.json"
QUESTIONS_PER_GAME = 10

# Sample question pool categorized by difficulty.
# You can expand this list later or load from external JSON file.
QUESTION_POOL = {
    "easy": [
        {
            "q": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "q": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "q": "What is 5 + 7?",
            "options": ["10", "11", "12", "13"],
            "answer": "12"
        },
        {
            "q": "What is the chemical symbol for water?",
            "options": ["O2", "H2", "CO2", "H2O"],
            "answer": "H2O"
        },
        {
            "q": "Which language is primarily used for Android app development (officially supported)?",
            "options": ["Swift", "Kotlin", "Ruby", "PHP"],
            "answer": "Kotlin"
        },
    ],
    "medium": [
        {
            "q": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
            "answer": "William Shakespeare"
        },
        {
            "q": "What is the largest mammal?",
            "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "answer": "Blue Whale"
        },
        {
            "q": "What is 12 × 8?",
            "options": ["90", "96", "88", "102"],
            "answer": "96"
        },
        {
            "q": "Which element has atomic number 1?",
            "options": ["Helium", "Oxygen", "Hydrogen", "Nitrogen"],
            "answer": "Hydrogen"
        },
        {
            "q": "Which inventor is credited with the telephone?",
            "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Guglielmo Marconi"],
            "answer": "Alexander Graham Bell"
        },
    ],
    "hard": [
        {
            "q": "What is the powerhouse of the cell?",
            "options": ["Ribosome", "Mitochondria", "Nucleus", "Golgi apparatus"],
            "answer": "Mitochondria"
        },
        {
            "q": "Which year did the World War II end?",
            "options": ["1945", "1944", "1946", "1942"],
            "answer": "1945"
        },
        {
            "q": "In computing, what does 'HTTP' stand for?",
            "options": ["HyperText Transfer Protocol", "High Transfer Text Protocol",
                        "Hyperlink Transfer Text Protocol", "Hyper Transfer Text Process"],
            "answer": "HyperText Transfer Protocol"
        },
        {
            "q": "What is the derivative of sin(x)?",
            "options": ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"],
            "answer": "cos(x)"
        },
        {
            "q": "Which gas is most abundant in Earth's atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"],
            "answer": "Nitrogen"
        },
    ]
}

# Time limits (seconds) mapped to difficulty
TIME_LIMITS = {
    "easy": 20,
    "medium": 15,
    "hard": 10
}


def input_with_timeout(prompt: str, timeout: int):
    """
    Read input from user with a timeout (works on all platforms using a thread).
    Returns None if timeout occurs.
    """
    q = queue.Queue()

    def _reader():
        try:
            ans = input(prompt)
            q.put(ans)
        except Exception:
            q.put(None)

    t = threading.Thread(target=_reader, daemon=True)
    t.start()
    try:
        ans = q.get(timeout=timeout)
        return ans
    except queue.Empty:
        return None


def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    try:
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_highscores(scores):
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)


def add_highscore(player_name, score, total, difficulty):
    records = load_highscores()
    records.append({
        "name": player_name,
        "score": score,
        "total": total,
        "percentage": round(score / total * 100, 1),
        "difficulty": difficulty,
        "date": datetime.now().isoformat()
    })
    # keep top 50
    records = sorted(records, key=lambda r: (-r["score"], -r["percentage"], r["date"]))[:50]
    save_highscores(records)


def print_highscores():
    recs = load_highscores()
    if not recs:
        print("No high scores yet.")
        return
    print("\n---- High Scores ----")
    for i, r in enumerate(recs[:10], start=1):
        print(f"{i}. {r['name']}: {r['score']}/{r['total']} ({r['percentage']}%) - {r['difficulty']} - {r['date']}")
    print("---------------------\n")


def assemble_quiz(difficulty):
    """
    Pick QUESTIONS_PER_GAME questions from pool based on difficulty selection.
    If difficulty == 'mixed', mix from all pools.
    """
    pool = []
    if difficulty == "mixed":
        for level in QUESTION_POOL:
            pool.extend(QUESTION_POOL[level])
    else:
        pool = QUESTION_POOL.get(difficulty, [])[:]
    if len(pool) < QUESTIONS_PER_GAME:
        # If not enough, fill from other pools
        for level in QUESTION_POOL:
            if level == difficulty:
                continue
            pool.extend(QUESTION_POOL[level])
    selected = random.sample(pool, QUESTIONS_PER_GAME)
    return selected


def shuffle_options(q_item):
    """
    Given a question dict with 'options' (list) and 'answer' (value),
    return list of tuples (label, option_text) and the label of correct answer.
    """
    opts = q_item["options"][:]
    random.shuffle(opts)
    labels = ["A", "B", "C", "D"]
    labeled = list(zip(labels, opts))
    # find correct label
    correct_label = None
    for lab, text in labeled:
        if text == q_item["answer"]:
            correct_label = lab
            break
    return labeled, correct_label


def lifeline_5050(labeled_opts, correct_label):
    """
    Return a reduced list of labeled options (keep correct + one random wrong).
    """
    # find wrong labels
    wrongs = [lab for lab, _ in labeled_opts if lab != correct_label]
    if len(wrongs) <= 1:
        return labeled_opts  # nothing to remove
    removed = random.sample(wrongs, k=2)
    reduced = [pair for pair in labeled_opts if pair[0] not in removed]
    # keep order A-D but filtered
    reduced = sorted(reduced, key=lambda x: x[0])
    return reduced


def lifeline_ask_audience(labeled_opts, correct_label):
    """
    Simulate audience poll with bias to correct option.
    Returns dict label -> percentage.
    """
    labels = [lab for lab, _ in labeled_opts]
    base = {lab: 0 for lab in labels}
    # bias: give correct option anywhere 50-70% depending on number of options
    correct_pct = random.randint(50, 75)
    remaining = 100 - correct_pct
    other_labels = [lab for lab in labels if lab != correct_label]
    if other_labels:
        splits = [random.random() for _ in other_labels]
        ssum = sum(splits)
        for lab, s in zip(other_labels, splits):
            base[lab] = int(round(remaining * (s / ssum)))
        # adjust rounding to sum exactly
        total = sum(base.values()) + correct_pct
        diff = 100 - total
        # adjust diff by adding/subtracting to a random non-correct label
        if other_labels:
            base[other_labels[0]] += diff
    base[correct_label] = correct_pct
    return base


def format_options(labeled_opts):
    return "   ".join([f"{lab}) {txt}" for lab, txt in labeled_opts])


def play_game():
    print("Welcome to the Quiz Game Show! 🎉")
    # players
    while True:
        try:
            num_players = int(input("Number of players (1-4): ").strip())
            if 1 <= num_players <= 4:
                break
            else:
                print("Please choose between 1 and 4 players.")
        except ValueError:
            print("Enter a valid integer.")

    players = []
    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ").strip() or f"Player{i}"
        players.append({
            "name": name,
            "score": 0,
            "lifelines": {"5050": True, "audience": True, "skip": True}
        })

    # difficulty
    diffs = ["easy", "medium", "hard", "mixed"]
    while True:
        d = input("Choose difficulty (easy / medium / hard / mixed): ").strip().lower()
        if d in diffs:
            difficulty = d
            break
        else:
            print("Invalid choice. Choose easy, medium, hard or mixed.")

    time_limit = TIME_LIMITS["medium"]
    if difficulty in TIME_LIMITS:
        time_limit = TIME_LIMITS[difficulty]
    print(f"Each question has {time_limit} seconds to answer. You may use lifelines once each per player.\n")

    # prepare questions
    quiz = assemble_quiz(difficulty)
    random.shuffle(quiz)  # extra shuffle
    # For reproducibility during debugging, you could set a seed.

    # Game loop: for each question, each player answers (turn-based)
    for q_index, q_item in enumerate(quiz, start=1):
        print(f"\n=== Question {q_index} of {QUESTIONS_PER_GAME} ===")
        # create randomized labeled options
        labeled_opts, correct_label = shuffle_options(q_item)
        # store original mapping for lifeline operations
        current_opts = labeled_opts[:]
        # track if player skipped (to avoid re-asking)
        for p in players:
            print(f"\nPlayer: {p['name']}")
            # If player already used skip for this question? skip is per-player, not per-question.
            # Display question and options
            used_this_question = False
            opts_for_player = current_opts[:]
            corr_label_for_player = None
            # Find correct label in current mapping
            for lab, txt in opts_for_player:
                if txt == q_item["answer"]:
                    corr_label_for_player = lab
                    break

            while True:
                print("\n" + q_item["q"])
                print(format_options(opts_for_player))
                print(f"(Lifelines left: 50/50={'Yes' if p['lifelines']['5050'] else 'No'}, "
                      f"Audience={'Yes' if p['lifelines']['audience'] else 'No'}, "
                      f"Skip={'Yes' if p['lifelines']['skip'] else 'No'})")
                print(f"You have {time_limit} seconds. Type A/B/C/D to answer, or 'L' to use a lifeline.")

                answer = input_with_timeout("Your choice: ", timeout=time_limit)
                if answer is None:
                    print("\nTime's up! ⏰ No answer recorded.")
                    # no score, break to next player
                    break
                answer = answer.strip().upper()
                if not answer:
                    print("No input detected. Try again.")
                    continue

                if answer == "L":
                    # Lifeline menu
                    available = [k for k, v in p['lifelines'].items() if v]
                    if not available:
                        print("No lifelines left.")
                        continue
                    print("Available lifelines:", ", ".join(available))
                    choice = input("Choose lifeline (5050 / audience / skip): ").strip().lower()
                    if choice not in ("5050", "audience", "skip"):
                        print("Invalid lifeline choice.")
                        continue
                    if not p['lifelines'].get(choice, False):
                        print("You already used that lifeline.")
                        continue
                    if choice == "5050":
                        # apply 50/50 to this player's options (makes it easier just for them)
                        opts_for_player = lifeline_5050(opts_for_player, corr_label_for_player)
                        print("Applied 50/50. Two wrong options removed.")
                        p['lifelines']['5050'] = False
                        # show reduced options then back to answering loop (no time reset)
                        continue
                    elif choice == "audience":
                        poll = lifeline_ask_audience(opts_for_player, corr_label_for_player)
                        print("Audience poll results:")
                        for lab, txt in opts_for_player:
                            pct = poll.get(lab, 0)
                            print(f"  {lab}) {txt} -> {pct}%")
                        p['lifelines']['audience'] = False
                        continue
                    elif choice == "skip":
                        # Skip this question for this player (no penalty, move on)
                        print("Question skipped. No points awarded for this question.")
                        p['lifelines']['skip'] = False
                        used_this_question = True
                        break  # exit answer loop for this player and go to next player
                else:
                    # normal answer path
                    if answer not in [lab for lab, _ in opts_for_player]:
                        print("Invalid option (or option not available after 50/50). Choose from displayed labels.")
                        continue
                    # map label to text
                    chosen_text = None
                    for lab, txt in opts_for_player:
                        if lab == answer:
                            chosen_text = txt
                            break
                    # check correctness
                    if chosen_text == q_item["answer"]:
                        print("Correct! ✅")
                        p['score'] += 1
                    else:
                        print(f"Wrong. ❌ Correct answer: {q_item['answer']}")
                    # after answering move to next player
                    used_this_question = True
                    break
            # end while for player answering
            # move to next player
        # end for players for this question
    # end for questions

    # Final scores
    print("\n=== Game Over ===")
    for p in players:
        total = QUESTIONS_PER_GAME
        perc = p['score'] / total * 100
        print(f"{p['name']}: {p['score']}/{total} ({perc:.1f}%)")
        # Save high score
        add_highscore(p['name'], p['score'], total, difficulty)

    print_highscores()
    print("Thanks for playing! 🎉")


if __name__== "_main_":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye.")
        sys.exit(0)