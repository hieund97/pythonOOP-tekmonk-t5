# Hướng Dẫn Sửa Lỗi Game Sudoku



## 1. Không nhập được số
### Nguyên nhân
1. Sự kiện nhập từ bàn phím (`KEYDOWN`) không được xử lý đúng. Em đang sử dụng `event.key in range(py.K_1, py.K_9)`, nhưng logic chuyển đổi số bị sai.
2. Giá trị `guess` không được gán khi nhấn phím.

### Sửa lỗi
Thay thế đoạn mã xử lý `KEYDOWN` bằng:
```python
if event.type == py.KEYDOWN and select:
    row, col = select
    if gaming[row][col] == 0:
        if py.K_1 <= event.key <= py.K_9:  # Kiểm tra nếu phím là từ 1-9
            guess = event.key - py.K_0  # Chuyển đổi key thành số
            gaming[row][col] = guess
            if guess != grid[row][col]:  # Nếu đoán sai
                wrong.append((row, col))
            elif (row, col) in wrong:  # Nếu đoán đúng
                wrong.remove((row, col))
        elif event.key == py.K_BACKSPACE:  # Xóa giá trị nếu nhấn Backspace
            gaming[row][col] = 0
```

---

## 2. Không tô màu ô được chọn
### Nguyên nhân
Em tính toán sai tọa độ cột (`col`) và dòng (`row`) khi nhấn chuột.

### Sửa lỗi
Thay thế đoạn xử lý sự kiện `MOUSEBUTTONDOWN` bằng:
```python
if event.type == py.MOUSEBUTTONDOWN:
    x, y = event.pos
    col, row = x // 80, y // 80  # Tính toán cột và dòng từ tọa độ
    if 0 <= row < 9 and 0 <= col < 9:  # Chỉ cho phép chọn trong lưới
        select = (row, col)
```

---

## 3. Sửa lỗi vẽ số trong lưới
### Nguyên nhân
Tọa độ vẽ số sai (cột và dòng không khớp với kích thước ô lưới).

### Sửa lỗi
Thay thế hàm `draw` bằng:
```python
def draw(screen, wrong_cells):
    for row in range(9):
        for col in range(9):
            if gaming[row][col] != 0:
                color = (0, 0, 0) if starter[row][col] != 0 else (100, 150, 255)
                text = font.render(str(gaming[row][col]), True, color)
                screen.blit(text, (col * 80 + 30, row * 80 + 20))  # Điều chỉnh tọa độ

    for row, col in wrong_cells:
        py.draw.rect(screen, (255, 0, 0), (col * 80, row * 80, 80, 80), 2)
```

---

## 4. Sai cách vẽ lại màn hình
### Nguyên nhân
Không cập nhật màn hình đúng cách trong vòng lặp chính, dẫn đến việc các thay đổi không hiển thị.

### Sửa lỗi
Thay thế vòng lặp chính bằng:
```python
while running:
    screen.fill(white)  # Xóa màn hình trước khi vẽ
    draw_grid()
    draw(screen, wrong)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
            running = False

        if event.type == py.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // 80, y // 80
            if 0 <= row < 9 and 0 <= col < 9:
                select = (row, col)

        if event.type == py.KEYDOWN and select:
            row, col = select
            if py.K_1 <= event.key <= py.K_9:
                guess = event.key - py.K_0
                gaming[row][col] = guess
                if guess != grid[row][col]:
                    wrong.append((row, col))
                elif (row, col) in wrong:
                    wrong.remove((row, col))
            elif event.key == py.K_BACKSPACE:
                gaming[row][col] = 0

    if select:
        row, col = select
        py.draw.rect(screen, (0, 0, 255), (col * 80, row * 80, 80, 80), 3)

    py.display.flip()  # Cập nhật màn hình
    oclock.tick(60)
```

