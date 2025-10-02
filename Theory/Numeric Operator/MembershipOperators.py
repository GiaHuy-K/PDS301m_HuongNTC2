# Toán tử membership trong Python giúp xác định xem một phần tử có nằm trong một đối tượng kiểu container (chứa nhiều phần tử bên trong) 
# hay không. Ví dụ, một danh sách (list), một tuple, hay một chuỗi (string) đều là những container.

# 1. Toán tử in
# Toán tử in được dùng để kiểm tra xem:

# Một chuỗi con (substring) có nằm trong một chuỗi lớn hơn hay không.
# Một phần tử bất kỳ có nằm trong một list hoặc tuple hay không.
# Một danh sách con (sub-list) hoặc tuple con (sub-tuple) có nằm trong một danh sách hoặc tuple lớn hơn hay không.
# Giả sử bạn có một danh sách các món ăn yêu thích, và bạn muốn kiểm tra xem một món ăn cụ thể có nằm trong danh sách đó hay không.
danh_sach_mon_an_yeu_thich = ["pho", "bun cha", "banh mi", "com tam"]

print ("pho" in danh_sach_mon_an_yeu_thich)    # Kết quả: True
print ("pizza" in danh_sach_mon_an_yeu_thich)  # Kết quả: False


# 2. Toán tử not in 
# Toán tử not in được dùng để kiểm tra xem một giá trị có không xuất hiện trong một chuỗi, list, tuple hoặc các đối tượng tương tự hay không.

# Để dễ hình dung, chúng ta hãy xem một ví dụ thực tế. Giả sử, bạn có một danh sách các loại trái cây:
danh_sach_trai_cay = ["xoai", "chuoi", "cam", "tao"]

# Kiểm tra xem "man" có KHÔNG nằm trong danh sách trái cây hay không
print("man", "not in", danh_sach_trai_cay, ":", "man" not in danh_sach_trai_cay)

# Kiểm tra xem "tao" có KHÔNG nằm trong danh sách trái cây hay không
print("tao", "not in", danh_sach_trai_cay, ":", "tao" not in danh_sach_trai_cay)