# Python có tổng cộng sáu toán tử Bitwise: &, |, ^, ~, << và >>. 
# Tất cả các toán tử này (ngoại trừ ~) đều là toán tử hai ngôi, nghĩa là chúng hoạt động trên hai toán hạng. 
# Mỗi toán hạng là một chữ số nhị phân (bit), có giá trị là 1 hoặc 0.

# Các toán tử Bitwise trong Python bao gồm:

# Toán tử AND Bitwise
# Toán tử OR Bitwise
# Toán tử XOR Bitwise
# Toán tử NOT Bitwise
# Toán tử dịch trái Bitwise
# Toán tử dịch phải Bitwise

print("Ví dụ về toán tử AND Bitwise trong Python")
x = 38
y = 15
print("x:", x, "y:",y, "x & y :", x & y)
print("giải thích:")
print ("x (nhị phân):", bin(x))
print ("y (nhị phân):", bin(y))
# Để dễ hình dung, chúng ta sẽ sử dụng định dạng 8-bit tiêu chuẩn cho mỗi số, nên x sẽ là 00100110 và y là 00001111. 
# Chúng ta sẽ thực hiện phép toán AND Bitwise trên từng cặp bit tương ứng:

#       0010 0110
# &     0000 1111
# ——————————————————
#       0000 0110
h = int("00000110",2)
print(h)

print("Ví dụ về toán tử OR Bitwise trong Python:")
a = 60
b = 13
print ("a:", a, "b:", b, "a|b:", a | b)
print ("a:", bin(a))
print ("b:", bin(b))
# Toán tử XOR Bitwise trong Python
# XOR là viết tắt của “exclusive OR” (hoặc loại trừ) là kết quả của phép toán OR trên hai bit sẽ là 1, nếu chỉ có một trong hai bit là 1.
# Nếu cả hai bit đều là 0, hoặc cả hai bit đều là 1, kết quả sẽ là 0. Cụ thể như sau:
# 0 ^ 0 kết quả là 0
# 0 ^ 1 kết quả là 1
# 1 ^ 0 kết quả là 1
# 1 ^ 1 kết quả là 0
print("Ví dụ về toán tử XOR Bitwise trong Python:")
a = 42
b = 27
print ("a:", a, "b:", b, "a^b:", a^b)

# Toán tử NOT Bitwise (~) là một phép toán tương đương ở mức bit của toán tử NOT logic. 
# Toán tử này đảo ngược từng bit của một số nguyên: bit 1 sẽ chuyển thành bit 0, và bit 0 sẽ chuyển thành bit 1. 
# Kết quả trả về là số bù (complement) của số ban đầu. Python sử dụng phương pháp bù 2.

# Đối với số nguyên dương, số bù được tính đơn giản bằng cách đảo ngược các bit. 
# Với số âm -x, số bù được biểu diễn bằng cách lấy mẫu bit của số (x - 1),
# sau đó đảo ngược tất cả các bit (bit 1 thành bit 0 và bit 0 thành bit 1). Vì thế (với biểu diễn 8 bit):

# -1 là số bù của (1 - 1) = số bù của 0 = “11111111“.
# -10 là số bù của (10 - 1) = số bù của 9 = số bù của “00001001” = “11110110“.
print("Ví dụ về toán tử NOT Bitwise trong Python:")
a = 60
print ("a:", a, "~a:", ~a)

# Toán tử dịch trái bit (<<) trong Python thực hiện việc dịch chuyển các bit trong biểu diễn nhị phân của một số sang trái một số lượng vị trí nhất định. 
# Số lượng vị trí cần dịch chuyển được chỉ định ở phía bên phải của ký hiệu <<. 
# Vì vậy, biểu thức x << 2 có nghĩa là dịch chuyển toàn bộ các bit trong biểu diễn nhị phân của x sang trái 2 vị trí.
print("Ví dụ về toán tử dịch trái bit:")
a = 60
print(bin(a)[2:])
print ("a:",a, "a<<2:", a<<2)
a = a << 2 
print(bin(a)[2:]) 

# Toán tử dịch phải bit trong Python
# Toán tử dịch phải bit (>>) trong Python thực hiện việc dịch các bit có trọng số nhỏ hơn về bên phải.
# Số bit dịch đi được xác định bởi số nằm bên phải của ký hiệu >>. 
# Vì vậy, khi viết x >> 2, điều đó có nghĩa là ta đang dịch hai bit trong biểu diễn nhị phân của x về bên phải.
a = 60
print ("a:", a, "a>>2:", a>>2)