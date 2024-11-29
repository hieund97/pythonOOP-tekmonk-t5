# Hướng Dẫn Chi Tiết Xây Dựng Game Matching Image Bằng Pygame

Game Matching Image là một trò chơi lật ô, nơi người chơi cần tìm và ghép các cặp hình ảnh giống nhau. Hướng dẫn này sẽ giải thích từng bước để xây dựng trò chơi bằng thư viện Pygame, dành cho cả những người mới bắt đầu.

---

## 1. Mục Tiêu

- **Tạo giao diện ô vuông 4x4:** Người chơi có thể lật ô vuông để xem hình ảnh ẩn.
- **Kiểm tra cặp hình ảnh:** Nếu hình ảnh trùng nhau, giữ nguyên. Nếu không, úp lại.
- **Tính điểm:** Cộng điểm khi ghép đúng cặp.
- **Kết thúc trò chơi:** Thông báo khi người chơi ghép xong toàn bộ cặp hình.

---

## 2. Cài Đặt Môi Trường

### Bước 1: Tải Hình Ảnh

Chuẩn bị 8 cặp hình ảnh (16 hình) và lưu chúng trong thư mục dự án. có thể thay hình ảnh bằng số

Ví dụ:
```
images/
  img1.png
  img2.png
  ...
  img8.png
```

---

## 3. Khởi Tạo Game

### Bước 1: Thiết Lập Màn Hình
- Tạo màn hình kích thước 800x600.
- Đặt tiêu đề và màu nền.

### Code Minh Họa
```python
import pygame

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matching Game")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cài đặt font chữ
font = pygame.font.SysFont("Comic Sans MS", 30)

# Vẽ nền
screen.fill(WHITE)
pygame.display.flip()
```

---

## 4. Tạo Các Ô Vuông

### Bước 1: Xác Định Kích Thước Và Vị Trí
- Mỗi ô vuông có kích thước 100x100 pixel.
- Cách nhau 20 pixel.
- Tạo lưới 4x4, với tọa độ được tính toán.

### Code Minh Họa
```python
CARD_SIZE = 100
MARGIN = 20

def create_card_positions():
    positions = []
    for row in range(4):
        for col in range(4):
            x = MARGIN + col * (CARD_SIZE + MARGIN)
            y = MARGIN + row * (CARD_SIZE + MARGIN)
            positions.append((x, y))
    return positions

card_positions = create_card_positions()
```

---

## 5. Tạo Cặp Hình Ảnh

### Bước 1: Xáo Trộn Hình Ảnh
- Tạo danh sách 8 hình ảnh, nhân đôi để có 16 hình.
- Xáo trộn danh sách để sắp xếp ngẫu nhiên.

### Code Minh Họa
```python
import random

def generate_pairs():
    symbols = list(range(8)) * 2  # Tạo 8 cặp
    random.shuffle(symbols)
    return symbols

pairs = generate_pairs()
```

---

## 6. Hiển Thị Ô Vuông Và Hình Ảnh

### Bước 1: Vẽ Ô Vuông
- Sử dụng `pygame.draw.rect` để vẽ các ô vuông trên màn hình.
- Ban đầu, ô vuông sẽ che hình ảnh.

### Bước 2: Hiển Thị Hình Ảnh Khi Lật
- Dùng `pygame.image.load` để tải hình ảnh.
- Khi ô được lật, hiển thị hình ảnh tại vị trí tương ứng.

### Code Minh Họa
```python
images = [pygame.image.load(f"images/img{i}.png") for i in range(8)]

def draw_cards():
    for index, pos in enumerate(card_positions):
        pygame.draw.rect(screen, BLACK, (pos[0], pos[1], CARD_SIZE, CARD_SIZE))
        # Nếu ô đã được lật, hiển thị hình ảnh
        if revealed[index]:
            img = pygame.transform.scale(images[pairs[index]], (CARD_SIZE, CARD_SIZE))
            screen.blit(img, pos)
        else:
            pygame.draw.rect(screen, BLACK, (pos[0], pos[1], CARD_SIZE, CARD_SIZE))

def update_screen():
    screen.fill(WHITE)
    draw_cards()
    pygame.display.flip()

revealed = [False] * 16
```

---

## 7. Xử Lý Tương Tác

### Bước 1: Lắng Nghe Sự Kiện
- Sử dụng vòng lặp `pygame.event.get` để lắng nghe sự kiện chuột.
- Kiểm tra vị trí chuột để xác định ô nào được chọn.

### Bước 2: Lật Ô Và Kiểm Tra Trùng Khớp
- Nếu hai ô được lật:
  - Kiểm tra cặp hình ảnh.
  - Nếu đúng, giữ nguyên.
  - Nếu sai, úp lại sau một khoảng thời gian.

### Code Minh Họa
```python
selected = []

def handle_click(pos):
    global selected
    for index, card_pos in enumerate(card_positions):
        rect = pygame.Rect(card_pos[0], card_pos[1], CARD_SIZE, CARD_SIZE)
        if rect.collidepoint(pos) and not revealed[index]:
            revealed[index] = True
            selected.append(index)
            if len(selected) == 2:
                if pairs[selected[0]] != pairs[selected[1]]:
                    pygame.time.wait(500)  # Đợi 500ms
                    revealed[selected[0]] = False
                    revealed[selected[1]] = False
                selected = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event.pos)
    update_screen()

pygame.quit()
```

---

## 8. Kết Thúc Trò Chơi

### Mục tiêu
- Khi tất cả ô được lật, thông báo người chơi thắng.
- Cho phép chơi lại hoặc thoát.

### Code Minh Họa
```python
def check_game_over():
    if all(revealed):
        print("You win!")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event.pos)
    update_screen()
    check_game_over()

pygame.quit()
```

---

