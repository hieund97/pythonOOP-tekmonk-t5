"""
    
Áp dụng kiến thức lớp và thuộc tính và phương thức. tạo 1 chương trình quản lý điểm số học sinh

Yêu cầu:
    - Phương thức: Tính điểm trung bình của học sinh
    - Phương thức: Hiển thị thông tin học sinh
    
Gợi ý:
    - Lớp std
    - Thuộc tính: ......
    - Thực hiện in ra điểm trung bình hoặc thông tin học sinh theo phương thức
    - Thực hiện hiển thị danh sách học sinh ( Gợi ý: Tạo 1 list chứa các học sinh)
    - Thực hiện hiển thị học sinh theo rank điểm TB
    
    name: string
    diem = {"toan": 10, "Hoa": 9, "TA": 9}
    

"""


class Student():

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def tinh_diem_tb(self, tham_so_truyen):
        diem_tb = (tham_so_truyen['toan'] + tham_so_truyen['Hoa'] + tham_so_truyen['TA']) / 3
        print(f"diem trung binh là: {diem_tb}")

    def thong_tin_hs(self, name, diem):
        print(f"Học sinh có tên là {name}")
        print(f"Có điểm toán là {diem['toan']}")
        print(f"Có điểm Hoá là {diem['Hoa']}")
        print(f"Có điểm TA là {diem['TA']}")


student1 = Student("Quyen", {"toan": 10, "Hoa": 9, "TA": 9})
student2 = Student("Dung", {"toan": 9, "Hoa": 10, "TA": 9})
student3 = Student("Tien", {"toan": 9, "Hoa": 9, "TA": 10})

print(student1.tinh_diem_tb(student1.name))
# print(student1.thong_tin_hs(student1.name, student1.score))
