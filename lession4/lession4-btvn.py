import math
import turtle

screen = turtle.Screen()
screen.title("Lá cờ Việt Nam")
screen.setup(width=600, height=400)
screen.bgcolor("red")

star = turtle.Turtle()
star.color("yellow")
star.speed(3)


def draw_star(turtle, size):
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

    a = caculate_star(180 - 144)

    fill_star(turtle, size, a)


def fill_star(turtle, size, a):
    a = 61.8
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(a)
    turtle.right(180 - (180 -2 * 36))
    turtle.forward(a)
    turtle.end_fill()


def caculate_star(angle):
    a = 50 / math.cos(math.pi / angle)

    return a


star.penup()
star.goto(-50, 50)
star.pendown()

# Vẽ ngôi sao và tô màu
draw_star(star, 100)

# Ẩn con trỏ turtle
star.hideturtle()

turtle.done()
