import numpy as np 
import os

print("Directory:", os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day10.31.2025")

# Tạo 1 mảng 1D có 5 số ngẫu nhiên (theo phân phối chuẩn)
a = np.random.randn(5) 

# Lưu mảng 'a' vào file tên là "textfile.txt"
np.savetxt("textfile.txt", a)

# Đọc file "textfile.txt" và in ra mảng đã đọc
print(np.loadtxt("textfile.txt"))

# mảng là 2D và có thể thay đổi được
# Tạo 1 mảng 2x2 chứa toàn số 0
A = np.zeros((2,2)) 
print("Initial A:")
print(A)
# [[0. 0.]
#  [0. 0.]]

# GÁN: 'C' và 'A' bây giờ cùng trỏ vào 1 chỗ
C = A 

# Thay đổi phần tử [0,0] của C thành 1
C[0,0] = 1 

# In C ra, ta thấy nó đã thay đổi
print("Modified C:")
print(C)

# [[1. 0.]
#  [0. 0.]]

# VÀ KHI IN A, ta thấy A CŨNG BỊ THAY ĐỔI THEO!
# print(A) # Nếu anh in A ở đây, kết quả cũng là [[1. 0.], [0. 0.]]


# 1. Tạo mảng 1D từ 0 đến 9
# 2. .reshape(2,5): Đổi hình dạng thành 2 hàng, 5 cột
a = np.arange(10).reshape(2,5)
print(a)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]

# --- Các thuộc tính ---

# .shape: Trả về hình dạng (số hàng, số cột)
# a.shape  -> kết quả là (2, 5)

# .size: Trả về tổng số phần tử
# a.size   -> kết quả là 10 (vì 2 * 5 = 10)

# .T (Transpose): Thuộc tính chuyển vị (lật hàng thành cột)
# a.T      -> kết quả là mảng 5 hàng, 2 cột

# .dtype: Trả về kiểu dữ liệu của các phần tử
# a.dtype  -> kết quả là dtype('int32') (số nguyên 32-bit)