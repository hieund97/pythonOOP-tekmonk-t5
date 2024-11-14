# import random

# names = ['Quang', 'Hung', 'Vinh', 'Yen']
# scores = {student:random.randint(1, 10) for student in names}

# pass_students = {student:score for (student, score) in scores.items() if score >= 6}

# print(pass_students)

"""
Chuyển đổi định dạng dữ liệu
Cho một danh sách các dictionary students, mỗi dictionary chứa thông tin name và score của học sinh. 
Tạo một dictionary mới với name là khóa và score là giá trị.

students = [
    {"name": "Alice", "score": 8},
    {"name": "Bob", "score": 5},
    {"name": "Charlie", "score": 7}
]

# Output: {'Alice': 8, 'Bob': 5, 'Charlie': 7}

"""

# students = [
#     {"name": "Alice", "score": 8},
#     {"name": "Bob", "score": 5},
#     {"name": "Charlie", "score": 7}
# ]


# out_put = {student['name']: student['score'] for student in students}
# print(out_put)


"""
paragraph = "Python is great. Python is easy to learn and powerful. Python programming is fun."
# Output: {'python': 3, 'great.': 1, 'easy': 1, 'learn': 1, 'and': 1, 'powerful.': 1, 'programming': 1, 'fun.': 1}

Viết một đoạn code để tạo một từ điển đếm số lần xuất hiện của mỗi từ trong một chuỗi paragraph, 
bỏ qua các từ có ít hơn 3 ký tự.

Gợi ý:

list = [1,2,3,1,1,1]

print(list.count(1)) # 4

split

"""

# paragraph = "Python is great. Python is easy to learn and powerful. Python programming is fun."


# out_put = {word: paragraph.split(" ").count(word)  for word in paragraph.split(" ") if len(word) > 3}
# print(out_put)


"""

Tính tổng giá trị đơn hàng theo khách hàng 
Cho danh sách các đơn hàng với cấu trúc tương tự như bài trước. 
Yêu cầu viết một đoạn code để tạo ra một từ điển tổng kết tổng giá trị đơn hàng
cho mỗi khách hàng, chỉ tính các khách hàng có tổng giá trị đơn hàng lớn hơn 100.

orders = [
    {"customer": "Alice", "item": "Laptop", "quantity": 1, "price": 1200},
    {"customer": "Bob", "item": "Mouse", "quantity": 5, "price": 25},
    {"customer": "Alice", "item": "Keyboard", "quantity": 1, "price": 100},
    {"customer": "Charlie", "item": "Monitor", "quantity": 2, "price": 150},
    {"customer": "Bob", "item": "Desk", "quantity": 1, "price": 200},
    {"customer": "Charlie", "item": "Chair", "quantity": 4, "price": 50},
    {"customer": "Charlie", "item": "Chair", "quantity": 2, "price": 50},
    {"customer": "Charlie", "item": "Chair", "quantity": 3, "price": 50},
]

quantity * price

# Output: {'Alice': 1300, 'Charlie': 500, 'Bob': 225}

"""



"""
Project cuối khoá sẽ làm 1 chương trình bằng Turtle hoặc Pygame
Yêu cầu:
    + Có sử dụng lập trình hướng đối tượng
    + Đọc và ghi kết quả (Điểm, số lần chơi, thời gian chơi) ra file
"""



