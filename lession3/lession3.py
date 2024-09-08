class Circle():
    def __init__(self, ban_kinh, pi):
        self.ban_kinh = ban_kinh
        self.pi = pi

    @property # getter
    def tinh_dien_tich(self):
        if self.ban_kinh is not None:
            return (self.ban_kinh ** 2) * self.pi
        else:
            print("Bán kính không được gán giá trị")
    
    @tinh_dien_tich.setter # setter -> gán giá trị cho 1 getter
    def tinh_dien_tich(self, value):
        self.ban_kinh = value
        
    @tinh_dien_tich.deleter
    def tinh_dien_tich(self):
        self.ban_kinh = None



circle1 = Circle(5, 3.14)
# circle1.ban_kinh = 10
circle1.tinh_dien_tich = 6

del circle1.tinh_dien_tich

# gán lại bán kính -> gọi lại 
# tạo ra 1 setter -> set lại giá trị cho bán kính -> diện tích thay đổi

# print(circle1.tinh_dien_tich())
print(circle1.tinh_dien_tich)
