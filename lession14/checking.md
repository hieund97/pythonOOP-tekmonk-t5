
### **1. Logic vẽ lưới**
- Logic vẽ các đường ngang và dọc có vấn đề:
  - Điều kiện `w**3 == 0` và `l**3 == 1` không hợp lý để quyết định độ dày của đường lưới.
  - Các đường dọc (`w`) có tọa độ y âm, khiến chúng không được hiển thị đúng cách.

#### **Cách sửa:**
Thay thế đoạn code vẽ lưới bằng logic chính xác hơn:

```python
for l in range(10):
    width = 2 if l % 3 == 0 else 1  # Đường dày hơn cho ranh giới 3x3
    py.draw.line(screen, black, (0, l * 80), (720, l * 80), width)  # Đường ngang
    py.draw.line(screen, black, (l * 80, 0), (l * 80, 720), width)  # Đường dọc
```

---

### **2. Lỗi logic vòng lặp chính**
- Vòng lặp chính (`while running`) không cập nhật màn hình đúng cách, ví dụ:
  - Hàm `draw()` không được gọi đúng vị trí để vẽ trạng thái lưới sau mỗi hành động.
  - `screen.blit()` được gọi không phù hợp (như khi vẽ text nhưng không có tọa độ chính xác).

#### **Cách sửa:**
Di chuyển hàm `draw(screen, wrong)` và thêm `py.display.flip()` vào cuối vòng lặp:

```python
while running:
    screen.fill(white)  # Làm sạch màn hình trước khi vẽ lại
    draw(screen, wrong)  # Vẽ lưới Sudoku
    for event in py.event.get():
        if event.type == QUIT:  # Thoát game
            py.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // 80, y // 80
            select = (row, col)
        if event.type == KEYDOWN and select:
            row, col = select
            if event.key in range(K_1, K_9):
                guess = int(event.unicode)
                if guess == grid[row][col]:
                    gaming[row][col] = guess
                else:
                    wrong.append((row, col))
            elif event.key == K_BACKSPACE:
                gaming[row][col] = 0
    py.display.flip()  # Cập nhật màn hình
    oclock.tick(20)  # Giới hạn FPS
```

---

### **3. Lỗi logic xác minh và điền số**
- Hàm `check()` kiểm tra số trong grid hoạt động đúng nhưng:
  - `prep(grid)` không chạy logic để tạo grid hoàn chỉnh chính xác.
  - Danh sách `liste` bị xáo trộn (do `random.shuffle`) nhưng không trả về giá trị.

#### **Cách sửa:**
Sửa hàm `prep()` để đảm bảo grid được điền đầy đủ và sửa `random.shuffle()`:

```python
def prep(grid):  # Tạo grid Sudoku
    numbers = list(range(1, 10))  # Sử dụng danh sách cố định
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                random.shuffle(numbers)  # Xáo trộn tại đây
                for num in numbers:
                    if check(grid, row, col, num):
                        grid[row][col] = num
                        if prep(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True
```

---

### **4. Các lỗi khác**
- **Vẽ sai kích thước số:** Kích thước số hiển thị trên lưới không đồng bộ với kích thước ô (80x80).
  - **Cách sửa:** Điều chỉnh tọa độ và kích thước font trong hàm `draw()`.
- **Không đặt `select`:** Khi không có ô nào được chọn, thao tác nhập sẽ gây lỗi.
  - **Cách sửa:** Kiểm tra giá trị `select` trước khi xử lý sự kiện.
