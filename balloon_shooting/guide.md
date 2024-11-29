# Hướng Dẫn Tạo Game Balloon Shooting Bằng Python Turtle

Trong game **Balloon Shooting**, người chơi sẽ điều khiển một mũi tên bắn các quả bóng bay trên màn hình. Trò chơi này sử dụng thư viện **Turtle** trong Python để vẽ đồ họa và xử lý các sự kiện.

---

## 1. Mục Tiêu

- **Điều khiển mũi tên:** Người chơi di chuyển mũi tên lên và xuống để ngắm.
- **Bắn bóng:** Bấm phím cách (Space) để bắn.
- **Tăng điểm:** Mỗi quả bóng bị bắn sẽ tăng điểm.
- **Kết thúc:** Trò chơi kết thúc khi người chơi bắn hết tất cả bóng.


---

## 3. Khởi Tạo Game

### Bước 1: Tạo Màn Hình
- Thiết lập cửa sổ game với kích thước và màu nền.

### Code Minh Họa
```python
import turtle

# Tạo màn hình
screen = turtle.Screen()
screen.title("Balloon Shooting Game")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)  # Tắt tự động cập nhật màn hình
```

---

## 4. Tạo Các Thành Phần Trong Game

### Bước 1: Tạo Người Chơi (Mũi Tên)
- Mũi tên sẽ được điều khiển bởi người chơi, di chuyển lên và xuống.

### Code Minh Họa
```python
# Tạo mũi tên
player = turtle.Turtle()
player.shape("triangle")
player.color("black")
player.penup()
player.goto(-350, 0)
player.setheading(0)  # Hướng sang phải

# Hàm di chuyển mũi tên
def move_up():
    y = player.ycor()
    if y < 250:  # Giới hạn di chuyển
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -250:
        player.sety(y - 20)

# Gắn phím điều khiển
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
```

### Bước 2: Tạo Các Quả Bóng
- Các quả bóng sẽ di chuyển từ phải sang trái.
- Khi bóng bị bắn trúng, nó sẽ biến mất.

### Code Minh Họa
```python
import random

# Tạo danh sách quả bóng
balls = []
for _ in range(5):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.speed(0)
    x = random.randint(100, 300)
    y = random.randint(-250, 250)
    ball.goto(x, y)
    balls.append(ball)
```

### Bước 3: Tạo Đạn
- Đạn sẽ xuất phát từ mũi tên và bay về phía các quả bóng.

### Code Minh Họa
```python
# Tạo đạn
arrow = turtle.Turtle()
arrow.shape("square")
arrow.color("black")
narrow.shapesize(stretch_wid=0.2, stretch_len=1.5)
narrow.penup()
narrow.speed(0)
narrow.hideturtle()

# Trạng thái đạn
arrow_state = "ready"

def fire_arrow():
    global arrow_state
    if arrow_state == "ready":
        arrow_state = "fire"
        arrow.goto(player.xcor(), player.ycor())
        arrow.showturtle()
```

---

## 5. Xử Lý Va Chạm

### Bước 1: Kiểm Tra Đạn Và Bóng
- Nếu đạn chạm vào bóng, bóng sẽ biến mất.

### Code Minh Họa
```python
# Hàm kiểm tra va chạm

def is_collision(t1, t2):
    distance = t1.distance(t2)
    return distance < 20

# Cập nhật bóng và đạn
for ball in balls:
    if is_collision(arrow, ball):
        ball.goto(random.randint(100, 300), random.randint(-250, 250))  # Tạo lại bóng ở vị trí mới
        arrow.hideturtle()
        arrow_state = "ready"
        score += 10
```

---

## 6. Thêm Hệ Thống Điểm

### Bước 1: Hiển Thị Điểm Số
- Cập nhật điểm mỗi khi người chơi bắn trúng bóng.

### Code Minh Họa
```python
# Tạo biến điểm
score = 0

# Hiển thị điểm
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
```

---

## 7. Vòng Lặp Chính

- Lắng nghe sự kiện từ bàn phím và cập nhật các thành phần trên màn hình.

### Code Minh Họa
```python
running = True
while running:
    screen.update()

    # Di chuyển các quả bóng
    for ball in balls:
        ball.setx(ball.xcor() - 2)
        if ball.xcor() < -400:
            ball.goto(random.randint(100, 300), random.randint(-250, 250))

    # Di chuyển đạn
    if arrow_state == "fire":
        arrow.setx(arrow.xcor() + 20)
        if arrow.xcor() > 400:
            arrow.hideturtle()
            arrow_state = "ready"

    # Kiểm tra va chạm
    for ball in balls:
        if is_collision(arrow, ball):
            ball.goto(random.randint(100, 300), random.randint(-250, 250))
            arrow.hideturtle()
            arrow_state = "ready"
            score += 10
            update_score()

    # Thoát game khi đóng cửa sổ
    for event in turtle.getcanvas().eventinfo():
        if event.type == "QUIT":
            running = False

turtle.done()
```

---

## 8. Cải Tiến

### Ý Tưởng Nâng Cao
- **Thêm âm thanh:** Phát nhạc nền hoặc âm thanh khi bắn trúng.
- **Tăng độ khó:** Tăng số lượng bóng hoặc tốc độ bóng.
- **Thời gian giới hạn:** Thêm bộ đếm thời gian.

Bạn có thể dựa trên hướng dẫn này để xây dựng một trò chơi thú vị hơn! Hãy thử tùy chỉnh theo ý tưởng của bạn.

