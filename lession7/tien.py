import random
import turtle

screen = turtle.Screen()
screen.title("Balloon Bursted")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

list_balloon = []

def create_balloon():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.speed(0)
    ball_x = random.randint(-390, 390)
    ball_y = random.randint(-290, 290)
    ball.goto(ball_x, ball_y)
    ball.dy = 2
    list_balloon.append(ball)


def move_ball():
    screen.update()
    for ball in list_balloon:
        ball_y = ball.ycor()
        ball_y += ball.dy
        ball.sety(ball_y)
        if ball_y > 300:
            ball.sety(-300)
            ball.setx(random.randint(-280, 280))


screen.tracer(0)
for i in range(1000):
    create_balloon()
    move_ball()
turtle.mainloop()
