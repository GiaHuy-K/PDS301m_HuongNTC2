# Các loại toán tử quan hệ trong Python
# Python còn có thêm hai toán tử quan hệ nữa là “==” (bằng nhau) và “!=” (không bằng nhau). 
# Như vậy, trong Python có tổng cộng sáu toán tử quan hệ, được liệt kê trong bảng sau:

# Toán tử	        Mô tả	            Ví dụ
# <	                Nhỏ hơn	            a<b
# >	                Lớn hơn	            a>b
# <=	        Nhỏ hơn hoặc bằng	    a<=b
# >=	        Lớn hơn hoặc bằng	    a>=b
# ==	            Bằng	            a==b
# !=	            Không bằng	        a!=b

print ("Cả hai toán hạng đều là số nguyên")
a = 5
b = 7
print ("a=", a, "b=", b, "a>b là", a > b)
print ("a=", a, "b=", b, "a<b là", a < b)
print ("a=", a, "b=", b, "a==b là", a == b)
print ("a=", a, "b=", b, "a!=b là", a != b)

print ("So sánh các chuỗi ký tự")
a = "Mèo"
b = "Meo"
print ("a=", a, "b=", b, "a < b là", a < b)
print ("a=", a, "b=", b, "a > b là", a > b)
print ("a=", a, "b=", b, "a == b là", a == b)
print ("a=", a, "b=", b, "a != b là", a != b)

print ("So sánh các tuple")
a = (1, 5, 2)
b = (1, 3, 8)
print ("a=", a, "b=", b, "a < b là", a < b)
print ("a=", a, "b=", b, "a > b là", a > b)
print ("a=", a, "b=", b, "a == b là", a == b)
print ("a=", a, "b=", b, "a != b là", a != b)
# giải thích :
# So sánh phần tử đầu tiên:

# a[0] = 1, b[0] = 1 → bằng nhau, nên bỏ qua.

# So sánh phần tử thứ hai:

# a[1] = 5, b[1] = 3.

# Vì 5 > 3 → kết quả so sánh được quyết định tại đây.

# => Python sẽ không cần so sánh a[2] và b[2] nữa.