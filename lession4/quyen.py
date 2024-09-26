import turtle as p
import math


# Red Background
p.goto(-100, 0)
p.fillcolor("#ff0000")
p.begin_fill()
p.forward(200)
p.left(90)
p.forward(100)
p.left(90)
p.forward(200)
p.left(90)
p.forward(100)
p.end_fill()

# Flag Pole
p.fillcolor("#000000")
p.begin_fill()
p.forward(200)
p.left(90)
p.forward(1)
p.left(90)
p.forward(200)
p.end_fill()

# Yellow Star
p.penup()
p.fillcolor("#ffff00")
p.begin_fill()
p.goto(-32.7254249, 60.63313510)
p.pendown()
p.right(90)
for x in range(5):
    p.forward(25)
    p.left(72)
    p.forward(25)
    p.right(144)
p.end_fill()

# Hide Pen
p.hideturtle()

p.mainloop()
