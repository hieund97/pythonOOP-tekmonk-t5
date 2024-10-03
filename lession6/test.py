import turtle
import random


def create_balloon():
    balloon = turtle.Turtle()
    balloon.shape("circle")
    balloon.penup()
    balloon.color(random.choice(['red', 'blue', 'green', 'yellow', 'purple', 'orange']))


random.randint(-250, 250)