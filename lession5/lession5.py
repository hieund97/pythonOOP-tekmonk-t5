import turtle


def move_up():
    turtle.setheading(90)  # Hướng lên
    turtle.forward(10)


def move_down():
    turtle.setheading(270)  # Hướng xuống
    turtle.forward(10)


def move_left():
    turtle.setheading(180)  # Hướng trái
    turtle.forward(10)


def move_right():
    turtle.setheading(0)  # Hướng phải
    turtle.forward(10)


def setup_screen():
    screen = turtle.Screen()
    screen.title("Turtle Key Control")
    screen.setup(width=600, height=600)

    # Đăng ký các phím để điều khiển
    screen.onkey(move_up, 'w')
    screen.onkey(move_down, 's')
    screen.onkey(move_left, 'a')
    screen.onkey(move_right, 'd')

    screen.listen()  # Bắt đầu lắng nghe sự kiện bàn phím
    screen.mainloop()


setup_screen()
