import random
import time
import turtle

# Cấu hình màn hình
screen = turtle.Screen()
screen.title("Balloon Bursted")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Cấu hình điểm số
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-200, 250)
score_display.write(f"Balloons Bursted: {score}", align="left", font=("Arial", 18, "normal"))

# Tạo danh sách quả bóng bay
balloons = []
number_of_balloons = 20


# Hàm tạo bóng bay
def create_balloon():
    new_balloon = turtle.Turtle()
    new_balloon.shape("circle")
    new_balloon.shapesize(1.5, 1)  # Để tạo hình elipse
    new_balloon.penup()
    new_balloon.speed(0)
    new_balloon.color(random.choice(['red', 'blue', 'green', 'yellow', 'purple', 'orange']))
    new_balloon.goto(random.randint(-280, 280), -300)
    new_balloon.dy = random.randint(1, 4)  # Tốc độ di chuyển lên của bóng
    balloons.append(new_balloon)


# Tạo quả bóng ban đầu
for _ in range(number_of_balloons):
    create_balloon()


# Xử lý khi nhấp vào bóng bay
def burst_balloon(x, y):
    global score
    for balloon in balloons:
        if balloon.isvisible() and balloon.distance(x, y) < 20:
            balloon.hideturtle()
            score += 1
            score_display.clear()
            score_display.write(f"Balloons Bursted: {score}",
                                align="left",
                                font=("Arial", 18, "normal"))


# Đặt sự kiện nhấp chuột
turtle.onscreenclick(burst_balloon)


# Cập nhật màn hình để di chuyển bóng bay
def move_balloons():
    screen.update()
    for balloon in balloons:
        y = balloon.ycor()
        y += balloon.dy
        balloon.sety(y)

        # Kiểm tra xem bóng bay có bay quá màn hình không
        if y > 300:
            balloon.sety(-300)
            balloon.setx(random.randint(-280, 280))


# Lặp di chuyển bóng bay
def game_loop():
    move_balloons()
    screen.ontimer(game_loop, 20)


# Bắt đầu vòng lặp trò chơi
screen.tracer(0)
game_loop()
screen.mainloop()
