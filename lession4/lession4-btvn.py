import math
import turtle

screen = turtle.Screen()
screen.title("Lá cờ Việt Nam")
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

    a = caculate_star(size, 180 -2 * 36)

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


def caculate_star(size, angle):
    a = math.sqrt(size**2 / (2 * (1 - math.cos(angle))))

    return a


star.penup()
star.goto(-50, 50)
star.pendown()

# Vẽ ngôi sao và tô màu
draw_star(star, 100)

# Ẩn con trỏ turtle
star.hideturtle()

turtle.done()