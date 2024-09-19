Để GitHub có thể hiển thị các công thức toán học chính xác, bạn có thể sử dụng cú pháp LaTeX trong Markdown hỗ trợ bởi các công cụ như MathJax. Tuy nhiên, GitHub không hỗ trợ trực tiếp việc hiển thị công thức toán học theo cú pháp LaTeX như trong file của bạn. Một cách để giải quyết là sử dụng các dịch vụ khác như GitLab hoặc Jupyter Notebook, nơi có hỗ trợ LaTeX tốt hơn.

Dưới đây là phiên bản sửa lại của file `readme.md`, chuyển đổi các công thức toán học LaTeX sang dạng văn bản để GitHub có thể hiển thị:

```markdown
# Giải bài toán tam giác

## Đề bài
Cho tam giác có cạnh đáy dài 100 đơn vị và hai góc ở đáy đều là 36 độ. Tìm độ dài hai cạnh còn lại của tam giác.

## Giải
Giả sử tam giác có các đỉnh là A, B, và C với AB là cạnh đáy có độ dài 100 đơn vị, và các góc tại A và B đều là 36 độ. Ta cần tìm độ dài của các cạnh AC và BC.

### Sử dụng định lý cosin
Định lý cosin cho tam giác ABC là:

```
c^2 = a^2 + b^2 - 2ab * cos(C)
```

Trong đó:
- a = b = AC = BC
- c = AB = 100
- C = 180 - 2 * 36 = 108 độ

Áp dụng định lý cosin:

```
100^2 = a^2 + a^2 - 2a^2 * cos(108 độ)
```

```
10000 = 2a^2 (1 - cos(108 độ))
```

```
a^2 = 10000 / (2 * (1 - cos(108 độ)))
```

```
a = sqrt(10000 / (2 * (1 - cos(108 độ))))
```

### Tính giá trị của cos(108)
Giá trị của cos(108 độ) có thể được tính bằng máy tính hoặc bảng giá trị cosin:

```
cos(108 độ) ≈ -0.309
```

Thay vào công thức:

```
a = sqrt(10000 / (2 * (1 - (-0.309))))
```

```
a = sqrt(10000 / (2 * (1 + 0.309)))
```

```
a = sqrt(10000 / (2 * 1.309))
```

```
a = sqrt(10000 / 2.618)
```

```
a ≈ sqrt(3819.5)
```

```
a ≈ 61.8
```

### Kết luận
Độ dài của hai cạnh còn lại của tam giác là khoảng 61.8 đơn vị.
```
