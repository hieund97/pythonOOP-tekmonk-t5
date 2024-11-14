# import csv
# import pandas
# import random

# with open("customers.csv", "r") as file:
#     reader = list(csv.reader(file))
#     reader.pop(0)
#     for i in range(3):
#         print(*random.choice(reader))
    
# data = pandas.read_csv("customers.csv")
# data_dict = data.to_dict()
# data_string = data.to_string()
# data_list_company = data['Company'].to_list() # chú ý: to_list áp dụng với 1 cột


# search_column = input("Nhập tên cột cần tìm: ")
# search_value = input("Nhập giá trị cần tìm: ")

# try:
#     data = pandas.read_csv("customers.csv") # đọc file
#     data_string = data.to_string() # chuyển toàn bộ thành string
#     data_list_column = data[search_column].to_list()
#     if search_value in data_list_column:
#         index = data_list_column.index(search_value)
#         print(data_string.split("\n")[index+1])
# except KeyError: 
#     print("không có cột cần tìm")
# except:
#     print("Có lỗi vui lòng thử lại")
    
    

# data_dict = {
#      'students': ['Quang', 'Minh', 'Thắng'],
#      'marks': [7, 8, 9]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('new_file.csv')


"""
Cho 1 dictionary có dữ liệu như sau:
data_dict = {
     'students': ['Quang', 'Minh', 'Thắng', "Hùng", "Tài", "Trường],
     'marks': [7, 8, 9, 6, 10, 5],
     'age': [10, 11, 12, 13, 14, 15],
     'gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male'],
     'city': ['HCM', 'Ha noi', 'Da nang', 'Hai Phong', 'Ca mau', 'HCM'],  
}

1. Chuyển dictionay trên thành CSV
2.Xây dựng chức năng tìm kiếm theo cột
tạo 2 input:
    + Nhập tên cột cần tìm:
    + Nhập giá trị tìm theo tên cột đó
In ra các user có giá trị cần tìm
Lưu ý: xử lý trường hợp người dùng nhập sai tên cột

VD: Cột students
    Quang
    -> thông tin của: Quang
"""





    
        
# 

"""
Xây dựng chức năng tìm kiếm theo cột
tạo 2 input:
    + Nhập tên cột cần tìm:
    + Nhập giá trị tìm theo tên cột đó


in ra các user có giá trị cần tìm

VD: First Name

    Sheryl
    
    -> thông tin của: Sheryl


"""

import sys
import pandas
import csv
data_dict = {
     'students': ['Quang', 'Minh', 'Thắng', "Hùng", "Tài", "Trường"],
     'marks': [7, 8, 9, 6, 10, 5],
     'age': [10, 11, 12, 13, 14, 15],
     'gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male'],
     'city': ['HCM', 'Ha noi', 'Da nang', 'Hai Phong', 'Ca mau', 'HCM'],  
}

data = pandas.DataFrame(data_dict)
data.to_csv('data_user.csv')

with open("data_user.csv", "r") as file:
    data_user = list(csv.reader(file))
    
data_index = data_user[0]

search_column = input("Nhập tên cột cần tìm: ")

column_index = None
for i in data_index:
    if i == search_column:
        column_index = data_index.index(i)

if column_index is None:
    print("Không có cột cần tìm")
    sys.exit() # câu lệnh để dừng chương trình python

search_value = input("Nhập giá trị cần tìm: ")
data_user.pop(0)    
found_user = 0
for i in data_user:
    if i[column_index] == search_value:
        found_user += 1
        print(f"{i[0]}. Tên: {i[1]} - Điểm {i[2]} - Tuoi: {i[3]} - Gioi tinh: {i[4]} - Thanh pho: {i[5]}")
   
if found_user == 0:
    print("Không tìm thấy giá trị")
    sys.exit()    

    
    

    