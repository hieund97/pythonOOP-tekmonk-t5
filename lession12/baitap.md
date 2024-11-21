
### Bài Tập 1: Tổng các số
Viết một hàm `sum_all(*args)` nhận vào số lượng đối số không xác định, và trả về tổng của tất cả các số được truyền vào.

```python
def sum_all(*args):
    # Viết mã tại đây
    pass

# Kết quả mong muốn
print(sum_all(1, 2, 3))  # Kết quả: 6
print(sum_all(4, 5, 6, 7, 8))  # Kết quả: 30
```

**Gợi ý**: Bạn có thể dùng vòng lặp `for` để duyệt qua từng phần tử trong `args` và cộng dồn giá trị.


### Bài Tập 2: Tìm giá trị lớn nhất
Viết một hàm `find_max(*args)` nhận vào số lượng đối số không xác định và trả về giá trị lớn nhất trong số đó.

```python
def find_max(*args):
    # Viết mã tại đây
    pass

# Kết quả mong muốn
print(find_max(1, 5, 3, 9, 2))  # Kết quả: 9
print(find_max(-10, -5, -2, -8))  # Kết quả: -2
```

**Gợi ý**: Dùng hàm `max()` hoặc tự viết thuật toán để tìm giá trị lớn nhất.


### Bài Tập 3: Thông tin cá nhân
Viết một hàm `display_info(**kwargs)` nhận vào nhiều đối số từ khóa và hiển thị thông tin đó dưới dạng `"key: value"`.

```python
def display_info(**kwargs):
    # Viết mã tại đây
    pass

# Kết quả mong muốn
display_info(name="Alice", age=25, city="Hanoi")
# input: name="Quang", age=20, address="Ha Noi", phone=123456789
#output: "Bạn Quang tuoi 20, song o Ha Noi, so dien thoai la 123456789"
```

**Gợi ý**: Bạn có thể dùng vòng lặp `for` để duyệt qua các cặp key-value trong `kwargs` và in ra.


### Bài Tập 4: Tính giá bán sau khi giảm giá
Viết một hàm `apply_discount(price, *args, **kwargs)` để tính giá cuối cùng sau khi áp dụng một số mức giảm giá nhất định. Các mức giảm giá sẽ là các phần trăm, được truyền vào dưới dạng `*args`, và loại thuế (`tax`) sẽ được truyền vào dưới dạng `**kwargs`.

- `price` là giá gốc.
- `*args` là các mức giảm giá theo phần trăm.
- `tax` là phần trăm thuế, giá trị mặc định là 10%.

```python
def apply_discount(price, *args, **kwargs):
    # Viết mã tại đây
    pass

# Kết quả mong muốn
print(apply_discount(1000, 10, 5, tax=8))  # Kết quả: giá sau khi giảm 15% và thêm thuế 8%
print(apply_discount(500, 20, tax=5))      # Kết quả: giá sau khi giảm 20% và thêm thuế 5%
```

**Gợi ý**:
1. Tính lần lượt từng mức giảm giá dựa trên `*args`.
2. Tính thuế nếu có `tax` trong `kwargs`.


### Bài Tập 5: Tạo chuỗi mô tả sản phẩm
Viết một hàm `describe_product(name, **kwargs)` để tạo một chuỗi mô tả sản phẩm. Tên sản phẩm là bắt buộc (`name`), còn các thuộc tính khác như `price`, `color`, `brand`... sẽ là tùy chọn, được truyền vào dưới dạng `**kwargs`.

```python
def describe_product(name, **kwargs):
    # Viết mã tại đây
    pass

# Kết quả mong muốn
print(describe_product("Laptop", brand="Dell", color="Silver", price=1200))
# Output:
# "Laptop - brand: Dell, color: Silver, price: 1200"
```

**Gợi ý**: Bạn có thể nối `name` với các cặp key-value trong `kwargs` để tạo thành chuỗi mô tả.


Chúc bạn luyện tập vui!