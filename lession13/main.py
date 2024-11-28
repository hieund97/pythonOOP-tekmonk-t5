# f = open("cau_hoi.txt", "r")



# f.close()


# with open("cau_hoi.txt", "r") as f:
#     f.read()
#     f.read(5)
#     f.readline()
#     f.readlines()
    
# with open("cau_hoi.txt", "w") as f:
#     f.write()
    
# with open("cau_hoi.txt", "a") as f:
#     f.write()
    
    
    
"""
r
a
w
x


a và w -> tự động tạo file nếu file không tồn tại
r -> báo lỗi nếu file không tồn tại
x -> báo lỗi nếu file đã tồn tại
"""

"""

Cho 1 dictionary chứa thông tin kho hàng:
dict = {
    "monitor": 150,
    "chair": 50,
    "keyboard": 100,
    "mouse": 25,
    "laptop": 1200,
    "desk": 200
}

yêu cầu: tạo 1 input người dùng nhập vào tên đồ muốn mua
 + đồ muốn mua tồn tại -> nhập số lượng -> tính ra giá cuối cùng -> Ghi vào file bill.txt
 + Đồ muốn mua không tồn tại -> In ra thông báo đồ bạn tìm đã hết hàng




"""


dict = {
    "monitor": 150,
    "chair": 50,
    "keyboard": 100,
    "mouse": 25,
    "laptop": 1200,
    "desk": 200
}

def process_order(dict):
    found = 0
    name_product = input("Nhập tên sản phẩm cần mua: ")
    if name_product not in dict:
        return found
    else:
        found += 1
        print(f"Sản phẩm {name_product} còn hàng")
        quantity = int(input("Nhập số lượng cần mua: "))
        total_price = dict[name_product]  * quantity
        
        export_bill(name_product, quantity, total_price)
    
    return found


def export_bill(name_product, quantity, total_price):
    with open("bill.txt", "a") as f:
        f.write(f"Sản phẩm {name_product} - Số lượng: {quantity} - Thành tiền: {total_price}\n")
        
def show_bill():
    with open("bill.txt", "r") as f:
        print(f.read())


while True:
    print("1. Mua hàng")
    print("2. Xem hóa đơn")
    print("3. Thoát")
    choice = int(input("Nhập lựa chọn: "))
    if choice == 1:
        found = process_order(dict)
        if found == 0:
            print("Sản phầm tạm hết hàng, vui lòng chọn lại")
            continue
    elif choice == 2:
        show_bill()
    else:
        break

