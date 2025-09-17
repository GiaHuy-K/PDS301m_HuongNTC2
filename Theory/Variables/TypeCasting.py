# Ép kiểu tường minh trong Python
# Như đã đề cập trước đó, ép kiểu ngầm định thường chỉ áp dụng cho việc chuyển đổi từ số nguyên (int) sang số thực (float).
# Để thực hiện các chuyển đổi khác như từ chuỗi (string) sang số nguyên,
# bạn cần sử dụng các hàm có sẵn của Python như int(), float(), và str(). Đây được gọi là ép kiểu tường minh
# hàm int(), float(), và str() là các hàm tích hợp sẵn trong Python,
print("Ép kiểu tường minh trong Python")
# Chuyển chuỗi nhị phân "1010" thành số nguyên (10)
binary_num = int("1010", 2)
print(binary_num)    # Kết quả: 10
# Chuyển chuỗi bát phân "12" thành số nguyên (10)
octal_num = int("12", 8)
print(octal_num)  # Kết quả: 10
# Chuyển chuỗi thập lục phân "A" thành số nguyên (10)
hex_num = int("A", 16)
print(hex_num) # Kết quả: 10