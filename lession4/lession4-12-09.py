import turtle as t


# t.forward(100)  # di chuyển rùa về phía trước 100 pixel
# t.right(90) 	# xoay phải 90 độ
# t.backward(50)  # di chuyển rùa về phía sau 50 pixel
# t.left(45)  	# xoay trái 45 độ

# t.left(20)


# t.penup()  # nhấc bút để không vẽ khi di chuyển
# t.goto(-150, 150)  # di chuyển tới vị trí mới
# t.pendown()

# t.forward(100)

def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)


draw_star(50)

t.penup()
t.goto(-200, 100)  # di chuyển tới vị trí mới
t.pendown()
draw_star(50)  # vẽ ngôi sao nhỏ hơn

t.penup()
t.goto(150, -150)
t.pendown()
draw_star(75)  # vẽ ngôi sao cỡ trung bình





# def draw_rect(width, height):
#     for _ in range(2):
#         t.forward(width)
#         t.left(90)
#         t.forward(height)
#         t.left(90)
        
# draw_rect(150, 70)

# t.left(90)
# t.forward(70)


# t.right(30)
# t.forward(150)
# t.right(120)
# t.forward(150)

# t.fillcolor('#0cf9e6')
# t.begin_fill()
# t.circle(100)
# t.end_fill()




# Vẽ hình tròn (mặt trời)

# def draw_sun(radius, count_sun_light):
#     t.penup()
#     t.goto(0, -radius)
#     t.pendown()

#     t.fillcolor("yellow")
#     t.begin_fill()
#     t.circle(radius)  # vẽ hình tròn với bán kính 100
#     t.end_fill()

#     # Vẽ tia sáng
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     for _ in range(count_sun_light):
#         t.forward(radius * 2)
#         t.backward(radius * 2)
#         t.right(360 // int(count_sun_light))

# draw_sun(120, 8)


# for _ in range(36):
# 	t.circle(50)
# 	t.right(10)




# def draw_petal():
#     for _ in range(2):
#         t.circle(100, 60)  # vẽ một phần hình tròn
#         t.left(120)

# for _ in range(6):
#     draw_petal()
#     t.right(60)  # xoay để vẽ cánh mới


t.mainloop()

