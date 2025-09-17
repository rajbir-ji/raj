import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
CELL = 25
GRID_WIDTH = WIDTH // CELL
GRID_HEIGHT = HEIGHT // CELL

# Colors
BG_COLOR = (35, 40, 60)
SNAKE_COLOR = (42, 202, 197)
HEAD_COLOR = (255, 218, 68)
FOOD_COLOR = (255, 83, 120)
SCORE_COLOR = (255, 255, 255)
GAME_OVER_COLOR = (255, 0, 80)

# Sounds (built-in beep style if no files)
def beep(freq=440, duration=120):
    try:
        import winsound
        winsound.Beep(freq, duration)
    except ImportError:
        # On non-Windows, fallback
        pass

try:
    eat_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "eat.wav"))
    gameover_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "gameover.wav"))
except:
    eat_sound = None
    gameover_sound = None

# Fonts
FONT = pygame.font.SysFont("consolas", 28, bold=True)
GAME_OVER_FONT = pygame.font.SysFont("arialblack", 46)

# Scoreboard file
SCORE_FILE = "snake_highscore.txt"
def load_high_score():
    try:
        with open(SCORE_FILE, "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    try:
        with open(SCORE_FILE, "w") as f:
            f.write(str(score))
    except:
        pass

def draw_text(surface, text, font, color, pos):
    img = font.render(text, True, color)
    surface.blit(img, pos)

# Game objects
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        self.dir = (1, 0)
        self.grow = False

    def move(self):
        head = (self.body[0][0] + self.dir[0], self.body[0][1] + self.dir[1])
        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_dir(self, newdir):
        # Prevent direct reverse
        if (self.dir[0] * -1, self.dir[1] * -1) != newdir:
            self.dir = newdir

    def collides(self, pos):
        return pos in self.body

    def out_of_bounds(self):
        x, y = self.body[0]
        return x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT

    def eats_self(self):
        return self.body[0] in self.body[1:]

    def get_head(self):
        return self.body[0]

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        while True:
            pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            if pos not in snake.body:
                return pos

    def respawn(self):
        self.position = self.random_position()

def play_sound(sound, freq=880, duration=120):
    if sound:
        sound.play()
    else:
        beep(freq, duration)

# Main game loop
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful 2D Snake Game")
clock = pygame.time.Clock()

high_score = load_high_score()

def main():
    global snake, food, high_score
    running = True
    snake = Snake()
    food = Food()
    score = 0
    move_delay = 120
    last_move = pygame.time.get_ticks()
    direction_queue = []

    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                save_high_score(high_score)
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction_queue.append((0, -1))
                elif event.key == pygame.K_DOWN:
                    direction_queue.append((0, 1))
                elif event.key == pygame.K_LEFT:
                    direction_queue.append((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    direction_queue.append((1, 0))
                elif event.key == pygame.K_r:
                    main()
                    return

        # Handle direction changes (queue)
        if direction_queue:
            snake.change_dir(direction_queue.pop(0))

        # Move the snake
        if pygame.time.get_ticks() - last_move > move_delay:
            snake.move()
            last_move = pygame.time.get_ticks()
            # Eating food
            if snake.get_head() == food.position:
                snake.grow = True
                play_sound(eat_sound, 880, 120)
                score += 1
                food.respawn()
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)
                # Speed up a little
                move_delay = max(55, move_delay-3)
            # Game over
            if snake.out_of_bounds() or snake.eats_self():
                play_sound(gameover_sound, 220, 300)
                draw_text(screen, "GAME OVER!", GAME_OVER_FONT, GAME_OVER_COLOR, (WIDTH//2-170, HEIGHT//2-50))
                draw_text(screen, f"Score: {score}", FONT, SCORE_COLOR, (WIDTH//2-60, HEIGHT//2+15))
                draw_text(screen, "Press R to Restart", FONT, SCORE_COLOR, (WIDTH//2-110, HEIGHT//2+55))
                pygame.display.flip()
                pygame.time.wait(200)
                waiting = True
                while waiting:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            waiting = False
                            running = False
                            save_high_score(high_score)
                            sys.exit()
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                            main()
                            return

        # Draw food
        fx, fy = food.position
        pygame.draw.rect(screen, FOOD_COLOR, (fx*CELL, fy*CELL, CELL, CELL), border_radius=8)

        # Draw snake
        for i, (x, y) in enumerate(snake.body):
            color = HEAD_COLOR if i == 0 else SNAKE_COLOR
            pygame.draw.rect(screen, color, (x*CELL, y*CELL, CELL, CELL), border_radius=12 if i == 0 else 7)

        # Draw grid (optional for style)
        for x in range(0, WIDTH, CELL):
            pygame.draw.line(screen, (50, 55, 75), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL):
            pygame.draw.line(screen, (50, 55, 75), (0, y), (WIDTH, y))

        # Draw score
        draw_text(screen, f"Score: {score}", FONT, SCORE_COLOR, (20, 15))
        draw_text(screen, f"High: {high_score}", FONT, SCORE_COLOR, (WIDTH-160, 15))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()