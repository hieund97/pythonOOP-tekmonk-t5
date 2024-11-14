import random
import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Balloon Shooter")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

balloons = []


#
def pop_balloon(balloon):
    balloon.hideturtle()
    balloons.remove(balloon)


# Tạo bóng với vị trí ngẫu nhiên
def create_balloon():
    balloon = turtle.Turtle()
    balloon.shape("circle")
    balloon.color("red")
    balloon.penup()
    balloon.speed(0)

    # Tạo vị trí ngẫu nhiên cho bóng
    x = random.randint(-250, 250)
    y = random.randint(-250, -100)

    balloon.goto(x, y)

    # Khi nhấn vào bóng, bóng sẽ nổ
    balloon.onclick(lambda x, y: pop_balloon(balloon))

    balloons.append(balloon)


# Tạo nhiều quả bóng
for _ in range(10):  # Tạo 10 quả bóng
    create_balloon()


# Cho bóng bay lên trên
def move_balloons():
    for balloon in balloons:
        y = balloon.ycor()
        y += random.randint(1, 3)
        balloon.sety(y)

        # Nếu bóng vượt khỏi màn hình, tạo bóng mới
        if y > 300:
            balloon.hideturtle()
            balloons.remove(balloon)
            create_balloon()

    screen.ontimer(move_balloons, 1)


# Bắt đầu di chuyển bóng
move_balloons()

# Chạy chương trình
turtle.mainloop()
