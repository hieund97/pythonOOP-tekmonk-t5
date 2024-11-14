import random
import turtle

# Thiết lập màn hình và các đối tượng
alla_breve = turtle.Screen()
alla_breve.setup(1500, 1000)

# Bật tracer và tắt tự động cập nhật màn hình
alla_breve.tracer(0)  # 0 để tắt tự động cập nhật

glissando = turtle.Turtle(shape="turtle")
glissando.penup()
sforzando = turtle.Turtle(shape="turtle")
sforzando.penup()
sforzando.hideturtle()
glissando.setheading(0)


# Hàm di chuyển lên xuống cho glissando
def upward():
    glissando.goto(0, glissando.ycor() + 20)


def downward():
    glissando.goto(0, glissando.ycor() - 20)


# Mảng lưu chướng ngại vật và các giá trị màu sắc và hình dạng
caesura = []
colors = [
    "#000000", "#ff0000", "#ffff00", "#00ff00", "#0000ff", "#00ffff", "#ff00ff", "#999999",
    "#0099ff", "#ff9900", "#ff0099", "#9900ff", "#99ff00", "#00ff99"
]
shapes = ["circle", "square", "triangle"]


# Kiểm tra va chạm giữa glissando và các chướng ngại vật
def check_collision():
    global caesura
    for i in caesura:
        if glissando.distance(i) < 20:  # Kiểm tra va chạm dựa trên khoảng cách
            sforzando.goto(-200, 0)
            sforzando.write("You lost", font=("MonoLisa", 50, "bold"))
            return True  # Trò chơi kết thúc khi va chạm
    return False


# Di chuyển tất cả chướng ngại vật
def move_obstacles():
    global caesura
    for obstacle in caesura:
        obstacle.forward(obstacle.speed_value)  # Di chuyển theo tốc độ ngẫu nhiên
        if obstacle.xcor() < -750:
            caesura.remove(obstacle)  # Xóa chướng ngại vật khi ra khỏi màn hình
            obstacle.hideturtle()


# Sinh chướng ngại vật mới với tốc độ ngẫu nhiên
def generate_obstacles():
    global caesura
    x = turtle.Turtle(shape=random.choice(shapes))
    x.penup()
    x.hideturtle()  # Ẩn rùa khi tạo
    x.goto(700, random.randint(-400, 400))  # Đặt vị trí ngẫu nhiên
    x.speed(0)  # Không liên quan đến tốc độ di chuyển
    x.color(random.choice(colors))
    x.setheading(180)  # Di chuyển từ phải sang trái
    x.showturtle()  # Hiện rùa sau khi đã thiết lập
    x.speed_value = random.uniform(0.5, 3)  # Gán tốc độ ngẫu nhiên nhỏ hơn để mượt mà hơn
    caesura.append(x)


# Cập nhật trò chơi liên tục
def update_game():
    if not check_collision():
        move_obstacles()
        if random.randint(1, 4) == 1:  # Xác suất tạo thêm chướng ngại vật
            generate_obstacles()
        alla_breve.update()  # Cập nhật màn hình sau mỗi lần gọi update_game
        alla_breve.ontimer(update_game, 10)  # Giảm thời gian cập nhật xuống 10ms để mượt mà hơn


# Bắt đầu trò chơi
def start_game():
    alla_breve.onkey(upward, 'Up')
    alla_breve.onkey(downward, 'Down')
    alla_breve.listen()
    update_game()


# Chạy trò chơi
start_game()
alla_breve.mainloop()


"""
chưa có tracer


turtle.right(144)
turtle.foward(61.8)

khi có tracer

screen.tracer(0)

turtle.right(144)
turtle.foward(61.8)
turtle.right(144)
turtle.foward(61.8)
turtle.right(144)
turtle.foward(61.8)


screen.update()



"""