import turtle
import random
import threading
import time
# from multiprocessing import Process
  
alla_breve = turtle.Screen()
glissando = turtle.Turtle(shape= "turtle")
glissando.penup()
sforzando = turtle.Turtle(shape= "turtle")
sforzando.penup()
sforzando.hideturtle()
glissando.setheading(0)

alla_breve.setup(1500, 1000)


def upward():
    glissando.goto(0, glissando.ycor()+10)

def downward():
    glissando.goto(0, glissando.ycor()-10)

caesura = []
colors = ["#000000", "#ff0000", "#ffff00", "#00ff00", "#0000ff", 
          "#00ffff", "#ff00ff", "#999999", "#0099ff", 
          "#ff9900", "#ff0099", "#9900ff", "#99ff00", "#00ff99"]
shapes = ["circle", "square", "triangle"]

def death():
    #  for i in caesura:
    #       if i.xcor() in range(3, -3) and i.ycor() in range(glissando.ycor+3, glissando.ycor-3):
    #            sforzando.goto(-200, 0)
    #            sforzando.write("You lost", font= ("MonoLisa", 50, "bold"))
               
    global caesura
    while True:
        for i in caesura:
            if glissando.distance(i) < 20: 
                sforzando.goto(-200, 0)
                sforzando.write("You lost", font=("MonoLisa", 50, "bold"))
                return
        time.sleep(0.01)

def generate():
      global caesura
      global colors
      global shapes
    #   game = True
    #   while game == True:
      for j in range(10):
            x = turtle.Turtle(shape= random.choice(shapes))
            x.hideturtle()
            x.penup()
            x.goto(700, random.randint(-400, 400))
            x.speed(random.randint(1,5))
            x.color(random.choice(colors))
            x.setheading(180)
            x.showturtle()
            x.forward(1520)
            alla_breve.onkey(upward, 'Up')
            alla_breve.onkey(downward, 'Down')
            alla_breve.listen()
            caesura.append(x)
            death()
            # generate()
def generator():
      global caesura
      global colors
      global shapes
    #   game = True
    #   while game == True:
      for j in range(10):
            x = turtle.Turtle(shape= random.choice(shapes))
            x.hideturtle()
            x.penup()
            x.goto(700, random.randint(-400, 400))
            x.speed(random.randint(1,6))
            x.color(random.choice(colors))
            x.setheading(180)
            x.showturtle()
            x.forward(1520)
            alla_breve.onkey(upward, 'Up')
            alla_breve.onkey(downward, 'Down')
            alla_breve.listen()
            caesura.append(x)
            death()
            # generator()



if __name__ == '__main__':
    nienta = threading.Thread(target= generate)
    niente = threading.Thread(target= generator)
    nienti = threading.Thread(target= death)
    nienta.start()
    niente.start()
    nienti.start()
    # nienta.join()
    # niente.join()
    # nienti.join()




alla_breve.mainloop()