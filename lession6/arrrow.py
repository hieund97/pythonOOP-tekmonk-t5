import turtle
import random

# Khởi tạo màn hình
window = turtle.Screen()
window.title("Balloon Shooter")
window.bgcolor("skyblue")
window.setup(width=600, height=600)
window.tracer(0)

# Lớp Balloon để đại diện cho mỗi quả bóng bay
class Balloon:
    def __init__(self, x, y, color):
        self.balloon = turtle.Turtle()
        self.balloon.shape("circle")
        self.balloon.color(color)
        self.balloon.penup()
        self.balloon.speed(0)
        self.balloon.goto(x, y)
        self.balloon.shapesize(stretch_wid=2, stretch_len=2)
        self.rise_speed = random.uniform(0.5, 1.5)  # Tốc độ bay lên của bóng bay
        self.popped = False

    def rise(self):
        if not self.popped:
            y = self.balloon.ycor()
            y += self.rise_speed
            self.balloon.sety(y)
            if y > 300:
                self.reset_position()

    def reset_position(self):
        self.balloon.goto(random.randint(-250, 250), random.randint(-300, -200))

    def pop(self, x, y):
        if self.balloon.distance(x, y) < 20:
            self.popped = True
            self.balloon.hideturtle()

# Lớp Game để quản lý trò chơi
class BalloonShooterGame:
    def __init__(self):
        self.balloons = []
        self.score = 0
        self.is_game_over = False

        # Tạo các quả bóng bay ngẫu nhiên
        for _ in range(10):
            x = random.randint(-250, 250)
            y = random.randint(-300, -100)
            color = random.choice(['red', 'blue', 'green', 'yellow', 'purple'])
            balloon = Balloon(x, y, color)
            self.balloons.append(balloon)

        # Hiển thị điểm số
        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def pop_balloon(self, x, y):
        for balloon in self.balloons:
            if not balloon.popped:
                balloon.pop(x, y)
                if balloon.popped:
                    self.score += 1
                    self.update_score()

    def play(self):
        while not self.is_game_over:
            window.update()

            # Di chuyển các quả bóng bay lên trên
            for balloon in self.balloons:
                balloon.rise()

            # Tạo lại các quả bóng bay đã nổ (pop)
            for balloon in self.balloons:
                if balloon.popped:
                    balloon.popped = False
                    balloon.balloon.showturtle()
                    balloon.reset_position()

# Khởi tạo và chơi game
game = BalloonShooterGame()

# Xử lý sự kiện click chuột
window.onscreenclick(game.pop_balloon)

# Vòng lặp chính
game.play()

# Đóng chương trình khi hoàn thành
turtle.done()
