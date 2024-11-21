import tkinter


def convert_C_to_F():
    do_C = float(entry_C.get())
    do_F = (do_C * 9/5) + 32
    entry_F.insert(1, do_F)

root = tkinter.Tk()
root.title("Ứng dụng tkinter đầu tiên")
root.minsize(width=1000, height=600)

entry_C = tkinter.Entry()
entry_C.grid(row=0, column=0, padx=10, pady=10)

label_C = tkinter.Label(text="Độ C").grid(row=0, column=1, padx=10, pady=10)

entry_F = tkinter.Entry().grid(row=1, column=0, padx=10, pady=10)
label_F = tkinter.Label(text="Độ F").grid(row=1, column=1, padx=10, pady=10)

button = tkinter.Button(text="Convert", command=convert_C_to_F).grid(row=2, column=0, padx=10, pady=10)


# Độ F = (Độ C × 9/5) + 32.




# thực thi logic ở giữa 2 câu lệnh này


root.mainloop()


