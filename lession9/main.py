"""

BTVN:
Bài 1: Tìm và thay thế từ trong file
Mục tiêu:
Viết một chương trình Python để tìm và thay thế một từ trong file text.txt.

Đọc nội dung file text.txt.
Thay thế tất cả các từ "Python" trong file thành "Java".
Ghi lại kết quả vào file text.txt.
Gợi ý:
Sử dụng phương thức replace() để thay thế từ.

Nội dung file text.txt:
Python là ngôn ngữ lập trình bậc cao đa năng. Triết lý thiết kế của nó nhấn mạnh khả năng đọc mã bằng cách sử dụng thụt lề đáng kể. Python 2.0 được ra mắt vào năm 2000. Python 3.0 được ra mẳt vào năm 2008, là bản sửa đổi lớn không hoàn toàn tương thích ngược với các phiên bản trước đó. Python 2.7.18, được phát hành vào năm 2020, là bản phát hành cuối cùng của Python 2


Bài 2: Trắc nghiệm tính cách:
Tạo 1 file cau_hoi.txt với nội dung là các câu hỏi
In ra từng câu hỏi tưng ứng là từng dòng trong file

Mặc định đáp án đúng là:
Câu 1 đáp án 1
Câu 2 đáp án 2
Câu 3 đáp án 3
Câu 4 đáp án 4

Tạo 1 input để người dùng nhập câu trả lời

Ghi kết quả vào 1 file ket_qua.txt
Ví dụ:
Câu 1: Đúng
Câu 2: Đúng
Câu 3: Sai
Câu 4: Sai

+ Hiển thị kết quả ra màn hình

Nội dung file cau_hoi.txt:
1. Người tốt bụng có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:
2 .Người đáng yêu có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:
3 .Người thật thà có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:
4. Người hay hót có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:

readlines  chuyển toàn bộ nội dung trong file thành list tương với các dòng
Mỗi phần tử trong list -> kiểu dữ liệu string
-> print -> list chứ kp print text


read -> in ra string -> tự động render các ký tự xuống dòng

thao tiếp với file

khái niệm path file

làm bài tập thực hành

thực hành thao tác với dữ liệu trong file csv

r -> read
w -> write
a -> append
x -> create

CRUD -> create, read, update, delete

Command line -> thực hiện với terminal

writelines -> ghi dư liệu vào file theo list -> chuyển toàn bộ phần tử của list thánh string, nối liền với nhau -> ghi vào file

["hello", "Hi", "Bye", "Python", "C++", "Java"]
"""

# import os
# # kiểm tra file có tồn tại hay không

# if os.path.exists('sesame.txt'):
#     os.remove('sesame.txt')
#     print("File has been removed")
# else:
#     print("File does not exist")




# question = "1. Người tốt bụng có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:\n2 .Người đáng yêu có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:\n3 .Người thật thà có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:\n4. Người hay hót có đặc điểm gì? 1-Béo, 2-Gầy, 3-Môi Dày, 4-Môi Mỏng:"

# with open("cau_hoi.txt", "w") as file:
#     file.write(question)
    
# with open("cau_hoi.txt", "r") as file:
#     list_question = file.readlines()
   
# index = 1
# list_answer = []
# for question in list_question:
#     print(question)
#     answer = int(input("Nhập câu trả lời: "))
#     if answer == index:
#         list_answer.append(f"Câu {index}: Đúng\n")
#     else:
#         list_answer.append(f"Câu {index}: Sai\n")
#     index += 1


# with open("dap_an.txt", "w") as file:
#         file.writelines(["hello\n", "Hi\n", "Bye\n", "Python\n", "C++\n", "Java\n"])
        


"""
Xây dựng chương trình quản lý người dùng và ghi lại nhật ký hoạt động
Mục tiêu:
Viết một chương trình Python có chức năng quản lý thông tin người dùng bao gồm:

Thêm người dùng mới.
Cập nhật thông tin người dùng.
Xóa người dùng.
Tìm kiếm người dùng.
Ngoài ra, chương trình sẽ ghi lại tất cả các thao tác (hoạt động) vào một file nhật ký activity.log, và có một chức năng riêng để xử lý file nhật ký này như:

Nhập tên, tuổi và email của người dùng.
Ghi lại thông tin vào file users.txt.
Ghi nhật ký hoạt động vào file activity.log.


Gợi ý

Tạo ra 1 hàm ghi vào file activity.text

tạo ra 1 hàm ghi vào file error.text

tao 4 hàm tương ứng CRUD với 1 user
    + Create -> lưu vào file list_user.txt
    + Read -> doc tu file list_user.txt
    + Update -> cap nhật user trong list_user.txt
    + Delete -> xóa user trong list_user.txt
Ghi vào file nhật ký activity.txt
nếu có lỗi sử dụng try except để ghi lỗi vào error.txt

"""

import datetime as d

def create_user(name, age, email):
    with open("list_user.txt", "a") as file:
        file.write(f"Tên: {name} - Tuổi: {age} - Email: {email}\n")
        
    print(f"Tạo người dùng thành công: Tên: {name} - Tuổi: {age} - Email: {email}")
        
def find_user(name):
    with open("list_user.txt", "r") as file:
        for line in file:
            if name in line:
                print(line)

def delete_user(name):
    with open("list_user.txt", "r") as file:
        data_user = file.readlines()
    
    for user in data_user:
        if name in user:
            data_user.remove(user)
    
    with open("list_user.txt", "w") as file:
        file.writelines(data_user) # writelines là ghi vào file ở chế độ list

def update_user(old_value, new_value):
    with open("list_user.txt", "r") as file:
        data_user = file.readlines()
        
    for user in data_user:
        if old_value in user:
            data_user = data_user[data_user.index(user)].replace(old_value, new_value)
            
            
    with open("list_user.txt", "w") as file:
        file.writelines(data_user)
        
def write_activity(activity):
    with open("activity.txt", "a") as file:
        file.write(f"[{d.datetime.now()}] {activity}\n")

def write_error(error):
    with open("error.txt", "a") as file:
        file.write(f"[{d.datetime.now()}] {error}\n")
        
while True:
    print("---MENU---")
    print("1. Tạo người dùng")
    print("2. Tìm kiếm người dùng")
    print("3. Cập nhật người dùng")
    print("4. Xóa người dùng")
    print("5. Thoát")
    
    choice = int(input("Nhập loại chức năng: "))
    
    if choice == 1:
        try:
            write_activity("bắt đầu tạo người dùng")
            name = input("Nhập tên người dùng: ")
            age = int(input("Nhập tuổi người dùng: "))
            email = input("Nhập email người dùng: ")
            create_user(name, age, email)
            write_activity("Tạo người dùng thành công")
        except ValueError:
            write_error("Lỗi khi nhập thông tin người dùng ")
        except:
            write_error("Lỗi khi tạo người dùng")
    elif choice == 2:
        try:
            write_activity("Tìm kiếm người dùng")
            name = input("Nhập tên người dùng: ")
            find_user(name)
            write_activity("Tìm kiếm thành công")
        except ValueError:
            write_error("Lỗi khi nhập thông tin")
        except:
            write_error("Lỗi khi tìm kiếm người dùng")
    elif choice == 3:
        try:
           write_activity("bắt đầu cập nhật người dùng")
           print("Nhập tên, email để cập nhật người dùng")
           old_value = input("Nhập giá trị cần tìm: ")
           new_value = input("Nhập giá trị cần sửa: ")
           update_user(old_value, new_value)
           write_activity("Cập nhật người dùng thành công")
        except ValueError:
            write_error("Lỗi khi nhập thông tin")
        except:
            write_error("Lỗi khi update người dùng")
    elif choice == 5:
        write_activity("Thoát chương trình")
        break