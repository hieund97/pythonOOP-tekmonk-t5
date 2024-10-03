import turtle
import time
import random
import numpy as np


# 20(0-19) rows and 12 columns(0-11)
grid = np.zeros((20,12))


# grid[0][0] = top left
# grid[0][11] = top right


win = turtle.Screen()
win.title('Tetris using Python 3 and Turtle')
win.bgcolor('black')
win.setup(600, 800)
win.tracer(0)
win.listen()


border = turtle.Turtle()
border.pensize(10)
border.up()
border.hideturtle()
border.goto(-130,240)
border.down()
border.color('white')
border.rt(90)
border.fd(490) # Down to -250
border.lt(90)
border.fd(260) # Right to +130
border.lt(90)
border.fd(490) # Up to 240
border.up()
border.goto(0,260)
border.write("TETRIS", align='center', font=('Courier', 36, 'normal'))


pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.color('red')
pen.goto(80,-300)
pen.write('Score: 0', align='center', font=('Courier', 24, 'normal'))




block_list = []
static_list = []


x_list = [-110, -90, -70, -50, -30, -10, 10, 30, 50, 70, 90, 110]
y_list = [150, 130, 110, 90, 70, 50, 30, 10, -10, -30, -50, -70,-90, -110, -130, -150,
               -170,-190, -210, -230]




class Block(turtle.Turtle):
    def __init__(self, block_list, static_list, grid):
        super().__init__(shape='square')


        self.shapesize(0.9, 0.9)
        
        self.up()
        self.goto(10, 250)
        self.list = block_list
        block_list.append(self)
        self.list2 = static_list
        self.grid = grid
        self.drop = 'go'
        self.colors = ['red', 'yellow', 'green', 'orange', 'blue', 'purple', 'lightblue']
        self.x_list = [-110, -90, -70, -50, -30, -10, 10, 30, 50, 70, 90, 110]
        self.y_list = [150, 130, 110, 90, 70, 50, 30, 10, -10, -30, -50, -70,-90, -110, -130, -150, -170,
                  -190, -210, -230]
        self.color(random.choice(self.colors))


        
    def move_right(self):
        for i in block_list:
            if i.xcor()<=90:
                i.goto(i.xcor()+20, i.ycor())
        




    def move_left(self):
        for i in block_list:
            if i.xcor()>=-90:
                i.goto(i.xcor()-20, i.ycor())




    def falling_block(self):
        if len(static_list)>0:
            for i in static_list:
                for j in block_list:
                    if j.ycor()-i.ycor() < 30 and j.xcor()==i.xcor():
                        j.drop = 'stop'
        for i in block_list:
            if i.ycor()>=-220 and i.drop == 'go':
                i.goto(i.xcor(), i.ycor()-20)


            # Set block as static and start new block
            # Add static to numpy grid
            else:
                i.list2.append(i)
                i.list.remove(i)
                print(i.xcor(),i.ycor())
                row = i.y_list.index(i.ycor())
                col = i.x_list.index(i.xcor())
                
                drop_piece(grid,col, row)
                finished_row(col,row)
                # Interesting to see how pieces fall into the grid
                print(grid) # Hash out to remove the grid
                new_block()




def new_block():
    block = Block(block_list, static_list, grid)




def drop_piece(grid, row, col):
    grid[col][row] = 1
    
def finished_row(col,row):
    global y_list
    global score
    global pen
    counter = 0
    
    for i in range(12):
        if grid[row][i] == 1:
            counter += 1
            y = y_list[row]  # yposition and column in numpy!!!
    #print('row', row, y)
    #print(counter)
    
    if counter == 12: # Full row
        score += 1
        pen.clear()
        pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
        
        for block in static_list:
            if block.ycor() == y:
                block.goto(1000,1000) # Remove blocks in row
            else:
                block.goto(block.xcor(), block.ycor()-20) # Drop remaining blocks
        for i in range(12):
            grid[row][i] = 0 # Remove all 1's in the row


        # Problem dropping 1s
        for i in range(row,0,-1):
            for j in range(12): # Drop all remaining 1's
                if grid[i-1][j] == 1:
                    grid[i][j] = 1
                    grid[i-1][j] = 0
                
                    
score = 0           
block = Block(block_list, static_list, grid)


win.onkey(block.move_right, 'Right')
win.onkey(block.move_left, 'Left')


while True:
    win.update()
    block.falling_block()
    time.sleep(0.1)
