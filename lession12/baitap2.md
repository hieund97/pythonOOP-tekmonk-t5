### Bài Tập: Ứng Dụng Máy Tính Cộng Trừ Đơn Giản

#### Mục tiêu:
Tạo một ứng dụng máy tính đơn giản với giao diện người dùng bằng `Tkinter` cho phép người dùng nhập hai số và chọn một phép toán (cộng hoặc trừ). Sau đó, khi nhấn nút, kết quả sẽ được hiển thị.

#### Yêu cầu:
- Giao diện gồm hai ô nhập cho hai số.
- Hai nút bấm: "Cộng" và "Trừ".
- Khi bấm "Cộng" hoặc "Trừ", kết quả của phép tính sẽ hiển thị trên màn hình.

#### Hướng dẫn:

1. **Tạo giao diện chính** với một cửa sổ và tiêu đề cho ứng dụng.
2. **Thêm hai ô nhập** để người dùng có thể nhập số thứ nhất và số thứ hai.
3. **Thêm hai nút bấm** cho phép chọn phép toán:
   - Nút "Cộng" để thực hiện phép cộng.
   - Nút "Trừ" để thực hiện phép trừ.
4. **Hiển thị kết quả** phép tính khi nhấn vào nút bấm.

#### Gợi ý mã:

Dưới đây là mã Python mẫu để bạn tham khảo và phát triển.

```python
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
```

#### Mở rộng:
- Bạn có thể thêm phép nhân, chia.
- Thêm kiểm tra đầu vào để đảm bảo người dùng không nhập giá trị không hợp lệ (như chia cho 0).
- Thêm phần màu sắc và giao diện cho đẹp mắt hơn. 

Chúc bạn luyện tập vui vẻ với `Tkinter`!