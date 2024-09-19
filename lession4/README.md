# Giải bài toán tam giác

## Đề bài
Cho tam giác có cạnh đáy dài 100 đơn vị và hai góc ở đáy đều là 36 độ. Tìm độ dài hai cạnh còn lại của tam giác.

## Giải
Giả sử tam giác có các đỉnh là \(A\), \(B\), và \(C\) với \(AB\) là cạnh đáy có độ dài 100 đơn vị, và các góc tại \(A\) và \(B\) đều là 36 độ. Ta cần tìm độ dài của các cạnh \(AC\) và \(BC\).

### Sử dụng định lý cosin
Định lý cosin cho tam giác \(ABC\) là:
$$
c^2 = a^2 + b^2 - 2ab \cdot \cos(C)
$$

Trong đó:
- \(a = b = AC = BC\)
- \(c = AB = 100\)
- \(C = 180 - 2 * 36 = 108)

Áp dụng định lý cosin:
$$
100^2 = a^2 + a^2 - 2a^2 \cdot \cos(108^\circ)
$$
$$
10000 = 2a^2 (1 - \cos(108^\circ))
$$
$$
a^2 = \frac{10000}{2(1 - \cos(108^\circ))}
$$
$$
a = \sqrt{\frac{10000}{2(1 - \cos(108^\circ))}}
$$

### Tính giá trị của cos(108)
Giá trị của cos(108) có thể được tính bằng máy tính hoặc bảng giá trị cosin:
$$
\cos(108^\circ) \approx -0.309
$$

Thay vào công thức:
$$
a = \sqrt{\frac{10000}{2(1 - (-0.309))}}
$$
$$
a = \sqrt{\frac{10000}{2(1 + 0.309)}}
$$
$$
a = \sqrt{\frac{10000}{2 \cdot 1.309}}
$$
$$
a = \sqrt{\frac{10000}{2.618}}
$$
$$
a \approx \sqrt{3819.5}
$$
$$
a \approx 61.8
$$

### Kết luận
Độ dài của hai cạnh còn lại của tam giác là khoảng 61.8 đơn vị.
