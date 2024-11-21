import tkinter as tik

screen = tik.Tk()
screen.title("Convert Fahrenheit to Celsius")
screen.minsize(width= 900, height= 700)

def convert():
    print(int(entry.get())/(9/5)+32)

entry = tik.Entry()
entry.grid(column= 0, row= 0, padx= 0, pady= 0)

label = tik.Label(text= "ºF", font= ("Arial", 24, "bold"))
label.grid(column= 1, row= 0, padx= 0, pady= 0)

button = tik.Button(text= "Enter", command= convert)
button.grid(column= 0, row= 1, padx= 0, pady= 0)

screen.mainloop()