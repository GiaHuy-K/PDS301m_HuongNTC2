# Ngoài hai giá trị True (đúng) và False (sai) quen thuộc, Python còn quy ước các giá trị sau tương đương với False:

# None (giá trị rỗng).
# Số 0 của tất cả các kiểu số (số nguyên, số thực,…).
# Các chuỗi rỗng (""), tuple rỗng (()), list rỗng ([]), dictionary rỗng ({}), và set rỗng (set()). 
# Các giá trị khác còn lại sẽ được coi là True.
# and, or , not
# and 
da_nop_hoc_phi = True  # Đã nộp học phí

da_co_chung_chi = False # Chưa có chứng chỉ

du_dieu_kien_dang_ky = da_nop_hoc_phi and da_co_chung_chi #Kiểm tra cả hai điều kiện

print (du_dieu_kien_dang_ky)

# or 
da_nop_hoc_phi = True
da_co_chung_chi = False

du_dieu_kien_dang_ky = da_nop_hoc_phi or da_co_chung_chi #Chỉ cần 1 trong hai

print (du_dieu_kien_dang_ky) # In kết quả kiểm tra

# Cách trình thông dịch đánh giá toán tử logic
# Khi trình thông dịch Python gặp một biểu thức dạng “x and y“, quy trình đánh giá diễn ra như sau:

# Đánh giá x trước: Python sẽ xem xét giá trị của x trước tiên.
# Nếu x là False: Ngay lập tức, Python sẽ trả về giá trị của x (tức là False) mà không cần quan tâm đến giá trị của y. 
# Vì trong phép toán and, chỉ cần một toán hạng là False thì cả biểu thức đã chắc chắn là False rồi.
# Nếu x là True: Khi này, Python mới cần đánh giá y. Kết quả trả về cuối cùng của biểu thức x and y chính là giá trị của y.


# Tương tự, đối với biểu thức “x or y“, trình thông dịch hoạt động theo cách sau:

# Đánh giá x trước: Python bắt đầu bằng việc xem xét giá trị của x.
# Nếu x là True: Ngay lập tức, Python sẽ trả về giá trị của x (tức là True) mà không cần đánh giá y. 
# Trong phép toán or, chỉ cần một toán hạng là True thì cả biểu thức đã chắc chắn là True.
# Nếu x là False: Python lúc này mới tiếp tục đánh giá y. Kết quả trả về cuối cùng của biểu thức x or y sẽ là giá trị của y.

# Toán tử logic với các điều kiện Boolean

x = 10
y = 20
print("x > 0 and x < 10:",x > 0 and x < 10)
print("x > 0 and y > 10:",x > 0 and y > 10)
print("x > 10 or y > 10:",x > 10 or y > 10)
print("x%2 == 0 and y%2 == 0:",x%2 == 0 and y%2 == 0)
print ("not (x+y>15):", not (x+y>15))
# Toán tử logic với các điều kiện không phải Boolean
# Toán tử logic cũng có thể được sử dụng với các toán hạng không phải kiểu boolean (ví dụ số, chuỗi). 
# Python coi các số khác 0, và chuỗi không rỗng tương đương với True , ngược lại 0 hoặc chuỗi rỗng tương đương với False. 
# Các quy tắc kết hợp toán tử logic vẫn giữ nguyên như trên. Ví dụ:
x = 10
y = 20
z = 0
print("x and y:",x and y)
print("x or y:",x or y)
print("z or x:",z or x)
print("y or z:", y or z)

# Toán tử logic với chuỗi và tuple
a="Xin chào"
b=tuple()
print("a and b:",a and b)
print("b or a:",b or a)
#  Toán tử logic so sánh các sequence (list)
# Hai đối tượng list trong ví dụ bên dưới đều không rỗng. 
# Do đó, x and y trả về đối tượng list thứ hai (y), còn x or y trả về đối tượng list thứ nhất (x).
x=[1, 2, 3]
y=[10, 20, 30]
print("x and y:",x and y)
print("x or y:",x or y)