import turtle
import random

def setup_turtles(colors):
    turtles = []
    spacing = 400 / len(colors)  # Tính khoảng cách dựa trên số lượng rùa
    start_x = -150
    start_y = -200 + spacing / 2

    for color in colors:
        racer = turtle.Turtle(shape="turtle")
        racer.penup()
        racer.color(color)
        racer.goto(start_x, start_y)
        racer.pendown()
        turtles.append(racer)
        start_y += spacing

    return turtles

def draw_finish_line():
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.goto(150, 200)
    finish_line.setheading(270)
    finish_line.speed(100)
    
    for i in range(10):  # Vẽ 10 ô vuông để tạo vạch đích
        if i % 2 == 0:
            finish_line.fillcolor("black")
        else:
            finish_line.fillcolor("white")
        finish_line.begin_fill()
        for _ in range(4):
            finish_line.forward(40)
            finish_line.right(90)
        finish_line.end_fill()
        finish_line.forward(40)

    finish_line.hideturtle()

def race(turtles):
    winner = None
    while True:
        for racer in turtles:
            step = random.randint(1, 20)
            racer.forward(step)
            x, y = racer.pos()
            if x >= 150:  # Vạch đích tại x = 150
                winner = racer.color()[0]  # Lấy màu của rùa chiến thắng
                return winner

def show_result(winner, bet):
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.goto(-100, 0)
    if bet == winner:
        pen.write(f"Bạn thắng! Rùa màu {winner} đã về đích đầu tiên!", font=("Arial", 16, "bold"))
    else:
        pen.write(f"Bạn thua! Rùa màu {winner} đã về đích đầu tiên, không phải rùa màu {bet}.", font=("Arial", 16, "bold"))

def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=400)

    # Định nghĩa màu sắc và thiết lập các rùa
    colors = ['red', 'blue', 'green', 'yellow']
    turtles = setup_turtles(colors)
    draw_finish_line()

    # Người dùng đặt cược
    bet = screen.textinput("Đặt cược vào một rùa", "Chọn màu rùa của bạn: " + ', '.join(colors)).lower()

    # Bắt đầu cuộc đua
    winner = race(turtles)

    # Hiển thị kết quả cho người dùng
    show_result(winner, bet)

    screen.mainloop()

main()
