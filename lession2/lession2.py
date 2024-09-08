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
    
    Sử dụng class method để khởi tạo 1 student từ 1 chuỗi
    
    VI du: Nguyen duc hieu, 10, 9, 9
    
    - Hiển thị xếp loại học sinh theo điểm TB:
        + HSG: >= 8.5
        + HSK: 7 -> 8.5
        + HSTT: 5 -> 7
        
    - Sử dụng Static method trả về 1 thông tin cho toàn bộ học sinh:
        + VD: Lớp có {len(student)} đang học python OOP
    - Xử lý nhập nhiều học sinh

"""


class Student():
    so_luong = 0

    def __init__(self, name, math, chemistry, physic):
        self.name = name
        self.math = math
        self.chemistry = chemistry
        self.physic = physic
        self.score = {
            'Toan': self.math,
            'hoa': self.chemistry,
            'ly': self.physic,
        }
        Student.so_luong += 1

    def __repr__(self) -> str:
        return f"{self.name}, 'toán {self.math}"

    @classmethod
    def from_string(cls, string):

        name, math, chemistry, physic = string.split(',')

        math = float(math)
        chemistry = float(chemistry)
        physic = float(physic)

        return cls(name, math, chemistry, physic)

    @staticmethod
    def thong_tin_chung():
        print(f"Lớp có {Student.so_luong} đang học python OOP")


string_student = input("Nhập thông tin học sinh vào đây")

student1 = Student.from_string(string_student)

print(student1)
print(Student.so_luong)
