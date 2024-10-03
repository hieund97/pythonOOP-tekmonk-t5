import turtle


def say_hello(x, y):
    star = turtle.Turtle()
    star.goto(x, y)
    star.begin_fill()  # bắt đầu tô màu
    for _ in range(5):
        star.forward(100)
        star.right(144)  # góc xoay để tạo ra ngôi sao 5 cánh
    star.end_fill()

turtle.onscreenclick(say_hello)

pen = turtle.Turtle()
pen.penup()

print(pen.isvisible())

balloon.distance(100, 200) < 20


turtle.mainloop()
