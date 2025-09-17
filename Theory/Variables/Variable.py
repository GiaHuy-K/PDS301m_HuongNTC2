# Xóa biến trong Python
# Trong Python, bạn có thể loại bỏ tham chiếu đến một đối tượng (object) trong bộ nhớ, hay còn gọi là xóa một biến, bằng cách sử dụng lệnh del
# . Cú pháp của lệnh del như sau:

# del bien_a # xóa một biến
# del bien_x, bien_y # xóa hai biến cùng lúc

print("Ví dụ về cách xóa một biến trong Python")
# Gán giá trị cho biến counter
counter = 100
# In giá trị của counter ra màn hình
print (counter)

# Xóa biến counter
del counter

# In lại giá trị của biến counter
# (Lúc này biến counter đã bị xóa nên sẽ gây ra lỗi)
# print (counter)


print("Cách xác định kiểu dữ liệu của biến")
# Trong Python, bạn có thể dễ dàng kiểm tra kiểu dữ liệu của một biến bằng cách sử dụng hàm type().
# Đây là một hàm được tích hợp sẵn trong Python, cho phép bạn biết được một biến đang chứa dữ liệu thuộc kiểu nào.
# Khai báo các biến với kiểu dữ liệu khác nhau
ho_ten = "Tèo"  # Chuỗi ký tự
so_luong = 20    # Số nguyên
gia_tri = 99.9  # Số thực

# Sử dụng hàm type() để xác định kiểu dữ liệu
print(type(ho_ten))
print(type(so_luong))
print(type(gia_tri))

print("Ép kiểu biến trong Python")
# Trong Python, bạn có thể chủ động chỉ định kiểu dữ liệu của một biến bằng cách sử dụng kỹ thuật ép kiểu (casting).
# Quá trình này cho phép bạn chuyển đổi một giá trị từ kiểu dữ liệu này sang một kiểu dữ liệu khác.
x = str(25)    # x sẽ là chuỗi '25'
y = int("30")  # y sẽ là số nguyên 30
z = float(5)  # z sẽ là số thực 5.0

print("x =", x)
print("y =", y)
print("z =", z)
print("Gán giá trị cho nhiều biến cùng lúc")
ho_ten, tuoi, nganh_hoc = "Huy", 20, "Công nghệ thông tin"

print(ho_ten)     # In ra Huy
print(tuoi)       # In ra 20
print(nganh_hoc)  # In ra Công nghệ thông tin

print("Biến cục bộ và biến toàn cục")
# Khai báo các biến toàn cục
x = 5
y = 10

def tinh_tong():
    tong = x + y
    return tong

# Gọi hàm và in kết quả
ket_qua = tinh_tong()
print("Tổng:", ket_qua)