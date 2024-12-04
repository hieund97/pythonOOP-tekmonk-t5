import random
import sys
import pygame as py
from pygame.locals import *

py.init()

# Cài đặt màn hình
screen_width = 720
screen_height = 720
white = (255, 255, 255)
black = (0, 0, 0)
screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Sudoku")

# Vẽ lưới Sudoku
for l in range(10):
    width = 2 if l % 3 == 0 else 1
    py.draw.line(screen, black, (0, l * 80), (720, l * 80), width)  # Đường ngang
    py.draw.line(screen, black, (l * 80, 0), (l * 80, 720), width)  # Đường dọc

font = py.font.SysFont("monospace", 25)
clock = py.time.Clock()
running = True

# Hàm kiểm tra hợp lệ
def check(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

# Hàm chuẩn bị grid Sudoku
def prep(grid):
    numbers = list(range(1, 10))
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if check(grid, row, col, num):
                        grid[row][col] = num
                        if prep(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Vẽ các số lên lưới
def draw(screen, grid, wrong_cells):
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                text = font.render(str(grid[row][col]), True, black)
                screen.blit(text, (col * 80 + 30, row * 80 + 20))
    for row, col in wrong_cells:
        py.draw.rect(screen, (255, 0, 0), (col * 80, row * 80, 80, 80), 3)

# Khởi tạo grid Sudoku
array = [[0 for _ in range(9)] for _ in range(9)]
prep(array)
grid = [row[:] for row in array]

starter = [row[:] for row in grid]
for _ in range(54):  # Xóa 54 ô để tạo lưới chơi
    row, col = random.randint(0, 8), random.randint(0, 8)
    starter[row][col] = 0
gaming = [row[:] for row in starter]
wrong = []
selected = None

# Vòng lặp chính
while running:
    screen.fill(white)
    draw_grid()
    draw(screen, gaming, wrong)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        if event.type == py.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // 80, y // 80
            selected = (row, col)

        if event.type == py.KEYDOWN and selected:
            row, col = selected
            if starter[row][col] == 0:  # Chỉ cho phép nhập số vào các ô trống
                if py.K_1 <= event.key <= py.K_9:
                    guess = event.key - py.K_0
                    if guess == grid[row][col]:
                        gaming[row][col] = guess
                        if (row, col) in wrong:
                            wrong.remove((row, col))
                    else:
                        wrong.append((row, col))
                elif event.key == py.K_BACKSPACE:
                    gaming[row][col] = 0
                    if (row, col) in wrong:
                        wrong.remove((row, col))

    py.display.flip()
    clock.tick(20)
