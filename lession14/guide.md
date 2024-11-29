# Hướng Dẫn Chi Tiết Xây Dựng Game Sudoku Bằng Pygame

## 1. Tạo Lưới Sudoku Tự Động (`generate_grid`)

### Mục tiêu
Tự động tạo lưới Sudoku ngẫu nhiên, đảm bảo tuân thủ các quy tắc của trò chơi.

### Phương pháp
1. **Tạo lưới đầy đủ:**
   - Sử dụng thuật toán đệ quy (backtracking) để điền lần lượt các số từ 1 đến 9.
   - Kiểm tra tính hợp lệ của số tại từng vị trí dựa trên các quy tắc Sudoku:
     - Số không được trùng trong hàng.
     - Số không được trùng trong cột.
     - Số không được trùng trong vùng 3x3.

2. **Xóa ngẫu nhiên các ô:**
   - Sau khi lưới được điền đầy đủ, chọn ngẫu nhiên các ô và xóa số (đặt giá trị bằng 0).
   - Xác định số ô bị xóa dựa trên mức độ khó của trò chơi.

### Code minh họa
```python
import random

def generate_grid():
    # Hàm kiểm tra số hợp lệ tại vị trí (row, col)
    def is_valid(grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    # Hàm đệ quy để điền lưới Sudoku
    def fill_grid(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if fill_grid(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    # Tạo lưới trống
    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)

    # Xóa bớt các số để tạo thử thách
    attempts = 30  # Số lượng ô cần xóa (càng cao, càng khó)
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = grid[row][col]
        grid[row][col] = 0

        # Đảm bảo lưới vẫn hợp lệ sau khi xóa
        attempts -= 1

    return grid
```

---

## 2. Kiểm Tra Số Hợp Lệ

### Mục tiêu
Đảm bảo rằng các số được nhập vào lưới tuân thủ các quy tắc của Sudoku:
- Không trùng trong hàng.
- Không trùng trong cột.
- Không trùng trong vùng 3x3.

### Cách kiểm tra
- Sử dụng hàm `is_valid` đã được viết trong quá trình tạo lưới. Hàm này kiểm tra số hiện tại có hợp lệ ở vị trí cụ thể hay không.

---

## 3. Thuật Toán Backtracking Trong Giải Sudoku (`solve`)

### Mục tiêu
Tìm lời giải cho lưới Sudoku hiện tại, sử dụng phương pháp thử và sai.

### Cách hoạt động
1. **Tìm ô trống:** Dò tìm lần lượt từ trái sang phải, trên xuống dưới để xác định ô chưa được điền.
2. **Thử điền số:** Điền từng số từ 1 đến 9 vào ô trống:
   - Nếu số hợp lệ, tiếp tục giải ô tiếp theo.
   - Nếu không hợp lệ, thử số tiếp theo.
3. **Quay lui:** Nếu không số nào hợp lệ, quay lui và thử lại từ ô trước đó.

### Code minh họa
```python
# Hàm giải Sudoku
def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True
```

---

## 4. Xử Lý Hiển Thị Lưới Sudoku

### Mục tiêu
Vẽ lưới Sudoku và hiển thị số trên màn hình bằng Pygame.

### Các bước chi tiết
1. **Cài đặt Pygame:**
   - Dùng lệnh `pip install pygame` để cài đặt thư viện nếu chưa có.
2. **Khởi tạo màn hình:**
   - Tạo màn hình với kích thước cố định, ví dụ `800x600`.
   - Sử dụng `pygame.display.set_mode` để tạo màn hình.
3. **Vẽ lưới:**
   - Sử dụng `pygame.draw.line` để vẽ các đường kẻ dọc và ngang, tạo thành lưới 9x9.
   - Tô đậm các đường kẻ chia vùng 3x3 bằng cách tăng độ dày của đường.
4. **Hiển thị số:**
   - Sử dụng `pygame.font.Font` để tạo font chữ.
   - Sử dụng `blit` để hiển thị từng số trong lưới tại vị trí tương ứng.

---

## 5. Tính Năng Đếm Ngược Thời Gian

### Mục tiêu
Tạo cảm giác áp lực bằng cách thêm thời gian giới hạn.

### Cách thực hiện chi tiết
1. **Tạo bộ đếm:**
   - Sử dụng `pygame.time.get_ticks()` để tính toán thời gian đã trôi qua kể từ khi trò chơi bắt đầu.
   - Trừ thời gian trôi qua từ tổng thời gian ban đầu để tính thời gian còn lại.
2. **Hiển thị thời gian:**
   - Hiển thị thời gian còn lại lên màn hình bằng Pygame.
   - Nếu thời gian về 0, thông báo người chơi thua.

---

## 6. Nhập Số Và Kiểm Tra Kết Quả

### Mục tiêu
Cho phép người chơi nhập số vào lưới và kiểm tra tính hợp lệ.

### Cách thực hiện chi tiết
1. **Xử lý sự kiện nhập số:**
   - Sử dụng vòng lặp `pygame.event.get()` để lắng nghe các sự kiện bàn phím.
   - Nếu người chơi chọn ô và nhập số từ 1-9, cập nhật số vào lưới.
2. **Kiểm tra tính hợp lệ:**
   - Sử dụng hàm `is_valid` để kiểm tra số vừa nhập có hợp lệ hay không.
   - Nếu số sai, tô viền ô màu đỏ và xóa số đã nhập.
   - Nếu đúng, giữ nguyên số trên lưới.

---

## 7. Xử Lý Kết Thúc Trò Chơi

### Mục tiêu
Kết thúc trò chơi khi lưới được điền đầy hoặc hết thời gian.

### Cách thực hiện chi tiết
1. **Kiểm tra lưới:**
   - Duyệt qua toàn bộ lưới để đảm bảo không còn ô trống.
   - Nếu lưới hoàn chỉnh và hợp lệ, thông báo thắng.
2. **Thông báo kết quả:**
   - Hiển thị thông báo kết quả (thắng/thua) lên màn hình.
   - Cho phép người chơi chơi lại hoặc thoát.

---



Hàm `solve` sử dụng **backtracking** để giải bài toán Sudoku. Đây là một thuật toán thử-sai (trial-and-error) giúp tìm giải pháp cho các bài toán bằng cách xây dựng từng bước các giải pháp hợp lệ và quay lại (backtrack) khi gặp sai lầm. Dưới đây là phân tích chi tiết hàm:

```python
def solve(grid):
    for row in range(GRID_SIZE):  # Lặp qua từng hàng
        for col in range(GRID_SIZE):  # Lặp qua từng cột
            if grid[row][col] == 0:  # Tìm ô trống (giá trị 0)
                for num in range(1, 10):  # Thử từng số từ 1 đến 9
                    if is_valid(grid, row, col, num):  # Kiểm tra số hợp lệ
                        grid[row][col] = num  # Đặt số vào ô
                        if solve(grid):  # Đệ quy giải các ô tiếp theo\n                            return True\n                        grid[row][col] = 0  # Nếu không thành công, xóa số và thử lại
                return False  # Nếu không có số nào hợp lệ, trả về False (backtrack)
    return True  # Nếu toàn bộ lưới được điền đúng, trả về True
```

### Cách hoạt động của Backtracking trong hàm này:

1. **Tìm ô trống đầu tiên:**
   - Bằng cách duyệt qua từng hàng và cột, hàm xác định vị trí của ô có giá trị `0` (chưa được điền).

2. **Thử điền số:**
   - Với mỗi ô trống, thử điền từng số từ `1` đến `9`.

3. **Kiểm tra tính hợp lệ:**
   - Hàm `is_valid` đảm bảo số được điền không trùng trong:
     - Hàng (`row`)
     - Cột (`col`)
     - Ô vuông con 3x3.

4. **Đệ quy giải tiếp:**
   - Sau khi điền một số hợp lệ, hàm tiếp tục gọi chính nó (`solve(grid)`) để giải các ô trống tiếp theo.

5. **Quay lại nếu gặp bế tắc:**
   - Nếu không số nào từ `1` đến `9` hợp lệ ở ô hiện tại:
     - Xóa số vừa thử (`grid[row][col] = 0`).
     - Quay lại ô trước để thử số khác.
   - Đây là bước **backtrack**.

6. **Hoàn thành:**
   - Khi tất cả các ô được điền đúng (không còn ô trống), hàm trả về `True`, kết thúc quá trình.

---

### Ví dụ minh họa:
- Lưới Sudoku ban đầu:
  ```
  5 3 0 | 0 7 0 | 0 0 0
  6 0 0 | 1 9 5 | 0 0 0
  0 9 8 | 0 0 0 | 0 6 0
  ---------------------
  8 0 0 | 0 6 0 | 0 0 3
  4 0 0 | 8 0 3 | 0 0 1
  7 0 0 | 0 2 0 | 0 0 6
  ---------------------
  0 6 0 | 0 0 0 | 2 8 0
  0 0 0 | 4 1 9 | 0 0 5
  0 0 0 | 0 8 0 | 0 7 9
  ```

- Hàm sẽ thử:
  - Ô `(0, 2)` thử lần lượt các số từ `1` đến `9`.
  - Giả sử `4` hợp lệ → điền `4` vào và đệ quy giải tiếp.

- Nếu giải tiếp đến bước không hợp lệ:
  - Xóa số `4` khỏi ô `(0, 2)`.
  - Thử số tiếp theo (`5`).

---

### Đặc điểm của Backtracking:

1. **Hiệu quả:** Backtracking chỉ thử các lựa chọn hợp lệ, không duyệt toàn bộ không gian tìm kiếm.
2. **Tổng quát:** Có thể áp dụng cho nhiều bài toán như Sudoku, N-queens, và phân hoạch đồ thị.
3. **Nhược điểm:** Với bài toán quá lớn, số lượng khả năng cần thử có thể tăng theo cấp số nhân.

Hàm `solve` sử dụng backtracking hiệu quả để tìm lời giải cho Sudoku, đảm bảo kiểm tra tất cả các khả năng một cách tối ưu.