import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Kết quả: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Kết quả: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Máy tính đơn giản")

# Tạo các nhãn và ô nhập cho số thứ nhất và số thứ hai
tk.Label(root, text="Số thứ nhất:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Số thứ hai:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Tạo nút "Cộng" và "Trừ"
add_button = tk.Button(root, text="Cộng", command=add)
add_button.grid(row=2, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="Trừ", command=subtract)
subtract_button.grid(row=2, column=1, padx=5, pady=5)

# Kết quả
result_label = tk.Label(root, text="Kết quả:")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Chạy vòng lặp chính
root.mainloop()