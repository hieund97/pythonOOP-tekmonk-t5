import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions and grid
WIDTH, HEIGHT = 540, 540
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.Font(None, 36)
TIMER_FONT = pygame.font.Font(None, 48)

# Function to check if a number can be placed in a specific cell
def is_valid(grid, row, col, num):
    # Check row
    for x in range(GRID_SIZE):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(GRID_SIZE):
        if grid[x][col] == num:
            return False

    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# Function to generate a random Sudoku grid
def generate_grid():
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for _ in range(20):  # Populate with 20 random numbers initially
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid(grid, row, col, num):
            grid[row][col] = num

    return grid

# Example Sudoku grid (generated)
START_GRID = generate_grid()

# Create a grid to modify during the game
grid = [row[:] for row in START_GRID]

def draw_grid(screen):
    """Draw the Sudoku grid lines."""
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK if x % (CELL_SIZE * 3) == 0 else GRAY, (x, 0), (x, HEIGHT))
        pygame.draw.line(screen, BLACK if x % (CELL_SIZE * 3) == 0 else GRAY, (0, x), (WIDTH, x))

def draw_numbers(screen, wrong_cells):
    """Draw the numbers on the Sudoku grid."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] != 0:
                color = BLACK if START_GRID[row][col] != 0 else BLUE
                text = FONT.render(str(grid[row][col]), True, color)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 4))

    # Highlight wrong cells
    for row, col in wrong_cells:
        pygame.draw.rect(
            screen, RED, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3
        )

def draw_timer(screen, time_left):
    """Draw the countdown timer on the screen."""
    timer_text = TIMER_FONT.render(f"Time Left: {time_left}s", True, RED)
    screen.blit(timer_text, (10, HEIGHT + 10))

def main():
    """Main game loop."""
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))  # Add space for timer
    pygame.display.set_caption("Sudoku")

    selected_cell = None
    wrong_cells = []
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    time_limit = 300  # 5 minutes in seconds

    while True:
        screen.fill(WHITE)

        # Calculate remaining time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        time_left = max(0, time_limit - elapsed_time)

        if time_left == 0:
            # Time's up
            end_text = TIMER_FONT.render("Time's up!", True, RED)
            screen.fill(WHITE)
            screen.blit(end_text, (WIDTH // 3, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // CELL_SIZE, y // CELL_SIZE
                if y < HEIGHT:
                    selected_cell = (row, col)

            if event.type == KEYDOWN and selected_cell:
                row, col = selected_cell
                if START_GRID[row][col] == 0:  # Allow modification only on empty cells
                    if event.key in range(K_1, K_9 + 1):
                        num = event.key - K_0
                        if is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if (row, col) in wrong_cells:
                                wrong_cells.remove((row, col))
                        else:
                            wrong_cells.append((row, col))
                            grid[row][col] = num
                            pygame.time.wait(500)  # Briefly show the wrong number
                            grid[row][col] = 0
                            wrong_cells.remove((row, col))
                    elif event.key == K_BACKSPACE:
                        grid[row][col] = 0
                        if (row, col) in wrong_cells:
                            wrong_cells.remove((row, col))

        # Draw the grid, numbers, and timer
        draw_grid(screen)
        draw_numbers(screen, wrong_cells)
        draw_timer(screen, time_left)

        # Highlight selected cell
        if selected_cell:
            row, col = selected_cell
            pygame.draw.rect(
                screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3
            )

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
