import random
import time
import turtle


# Lớp Obstacle đại diện cho chướng ngại vật
class Obstacle:

    def __init__(self, speed):
        self.rect = turtle.Turtle()
        self.rect.shape("square")
        self.rect.shapesize(stretch_wid=2, stretch_len=random.randint(2, 4))
        self.rect.color(random.choice(["red", "green", "blue", "yellow", "purple"]))
        self.rect.penup()
        self.rect.speed(0)
        self.rect.goto(300, random.randint(-250, 250))  # Vị trí xuất phát của chướng ngại vật
        self.speed = speed

    def move(self):
        x, y = self.rect.position()
        x -= self.speed
        self.rect.setx(x)

    def destroy(self):
        self.rect.hideturtle()

    def get_position(self):
        return self.rect.position()


# Lớp Player đại diện cho con rùa của người chơi
class Player:

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("green")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(-250, 0)  # Vị trí ban đầu của rùa

    def move_up(self):
        y = self.turtle.ycor()
        if y < 250:  # Giới hạn di chuyển không vượt quá màn hình
            self.turtle.sety(y + 20)

    def move_down(self):
        y = self.turtle.ycor() # lấy giá trị y hiện tại
        if y > -250:  # Giới hạn di chuyển không vượt quá màn hình
            self.turtle.sety(y - 20)

    def move_left(self):
        x = self.turtle.xcor() # lấy giá trị x hiện tại
        if x > -280:  # Giới hạn di chuyển không vượt quá màn hình
            self.turtle.setx(x - 20)

    def move_right(self):
        x = self.turtle.xcor()
        if x < 280:  # Giới hạn di chuyển không vượt quá màn hình
            self.turtle.setx(x + 20)

    def get_position(self):
        return self.turtle.position()


# Lớp Game để quản lý toàn bộ trò chơi
class TurtleGame:

    def __init__(self):
        # Thiết lập cửa sổ
        self.window = turtle.Screen()
        self.window.title("Turtle Avoid Obstacle Game")
        self.window.bgcolor("lightblue")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        # Người chơi và danh sách chướng ngại vật
        self.player = Player()
        self.obstacles = []
        self.score = 0
        self.game_over = False

        # Gán phím điều khiển
        self.window.listen()
        self.window.onkey(self.player.move_up, "Up")
        self.window.onkey(self.player.move_down, "Down")
        self.window.onkey(self.player.move_right, "Right")
        self.window.onkey(self.player.move_left, "Left")

    def create_obstacle(self):
        speed = random.randint(3, 9)
        new_obstacle = Obstacle(speed)
        self.obstacles.append(new_obstacle)

    def check_collision(self, obstacle):
        player_pos = self.player.get_position()
        obstacle_pos = obstacle.get_position()
        # Kiểm tra khoảng cách giữa rùa và chướng ngại vật để xem có va chạm không
        if abs(player_pos[0] - obstacle_pos[0]) < 30 and abs(player_pos[1] - obstacle_pos[1]) < 30:
            self.game_over = True

    def play(self):
        while not self.game_over:
            self.window.update()  # Cập nhật màn hình

            # Tạo chướng ngại vật mới ngẫu nhiên
            if random.randint(1, 50) == 1:
                self.create_obstacle()

            # Di chuyển chướng ngại vật
            for obstacle in self.obstacles:
                obstacle.move()
                self.check_collision(obstacle)

            # Loại bỏ chướng ngại vật đã đi qua màn hình
            self.obstacles = [
                obstacle for obstacle in self.obstacles if obstacle.get_position()[0] > -300
            ]

            # Tạm dừng để kiểm soát tốc độ game
            time.sleep(0.02)

        # Kết thúc trò chơi
        self.end_game()

    def end_game(self):
        self.window.clear()  # Xóa tất cả để chuẩn bị cho thông báo "Game Over"
        self.window.bgcolor("black")
        game_over_turtle = turtle.Turtle()
        game_over_turtle.color("red")
        game_over_turtle.hideturtle()
        game_over_turtle.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
        self.window.update()


# Khởi tạo và chơi game
if __name__ == "__main__":
    game = TurtleGame()
    game.play()
    turtle.done()
