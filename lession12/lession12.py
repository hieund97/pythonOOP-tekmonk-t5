# def show_info_student(x, y, z): # default value
#     sum = x + y + z
    
#     return sum


# ket_qua = show_info_student(10, 20)
# print(ket_qua)


# def sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
    
# ket_qua = sum(10,20,30,40,50, 60, 70, 80, 90)

# # () # không chỉnh sửa được giá trị bên trong
# # [] # list chỉnh sửa hoặc thêm bớt giá trị bình thường
# print(ket_qua)


def sum(**kargs): # gom các giá trị vào thành 1 dictionary
    print(kargs)
    for key, value in kargs.items():
        print(f"{key}: {value}")
    


def find_max(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
    print(max)


# input: name="Quang", age=20, address="Ha Noi", phone=123456789
#output: "Bạn Quang tuoi 20, song o Ha Noi, so dien thoai la 123456789"


def display_info(**kwargs):
    print(f"Bạn {kwargs['name']} tuoi {kwargs['age']}, song o {kwargs['address']}, so dien thoai la {kwargs['phone']}")
    


display_info(name="Quang", age=20, address="Ha Noi", phone=123456789)
