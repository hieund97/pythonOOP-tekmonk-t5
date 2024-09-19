import turtle
t = turtle.Turtle()

def draw_petal():
    for _ in range(2):
        t.circle(100, 60)  # vẽ một phần hình tròn
        t.left(120)

for _ in range(6):
    draw_petal()
    t.right(60)  # xoay để vẽ cánh mới

t.mainloop()