import turtle as t

from random import random
t.bgcolor("lightblue")  # đặt màu nền là màu xanh dương nhạt
t.pencolor("red")  # đặt màu bút vẽ là màu đỏ
t.fillcolor("yellow")  # đặt màu tô bên trong là màu vàng

t.penup()  # nhấc bút để không vẽ khi di chuyển
t.goto(-150, 150)  # di chuyển tới vị trí mới
t.pendown() 


# for i in range(2):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
    
# for x in range(100) :
#     t.forward(x)
#     t.left(91)
    
# for x in range(100) :
#     t.circle(x)
#     t.left(91)

# t.begin_fill()  # bắt đầu tô màu
# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# t.end_fill()  # kết thúc tô màu

def draw_star(size):
    t.begin_fill()  # bắt đầu tô màu
    for _ in range(5):
        t.forward(size)
        t.right(144)  # góc xoay để tạo ra ngôi sao 5 cánh
    t.end_fill()  # kết thúc tô màu

t.fillcolor("yellow")  # màu tô vàng
t.pencolor("blue")  # màu bút xanh
draw_star(100)  # vẽ ngôi sao với kích thước 100


    
t.mainloop()
