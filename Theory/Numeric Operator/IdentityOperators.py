# Toán tử nhận dạng trong Python dùng để so sánh hai đối tượng, xác định xem hai đối tượng có cùng vị trí trên bộ nhớ,
# và cùng kiểu dữ liệu (data type) hay không.
# Trong Python có 2 loại toán tử nhận dạng là is và is not.

# 1. Toán tử is
# Toán tử is sẽ trả về giá trị True nếu hai đối tượng ở hai bên toán tử cùng chia sẻ một vị trí ô nhớ. 
# Để xác định vị trí ô nhớ của một đối tượng, chúng ta có thể dùng hàm id().
# Nếu id() của hai biến cho ra kết quả giống nhau, thì toán tử is trả về True.

# Để bạn dễ hình dung, hãy tưởng tượng hai người bạn cùng chung nhau một phòng trọ. 
# Dù hai bạn là hai cá thể riêng biệt, nhưng khi nói đến địa chỉ, thì cả hai bạn sẽ có chung một địa chỉ.


xe_cua_ban = ["Honda", "mau_do", 2023]
# Bạn của bạn mượn xe của bạn và vẫn sử dụng chính chiếc xe đó.
xe_ban_muon = xe_cua_ban
# Tạo một chiếc xe y hệt
xe_moi_mua_giong_het = ["Honda", "mau_do", 2023]
# So sánh sử dụng 'is'
print(xe_cua_ban is xe_ban_muon)
print(xe_cua_ban is xe_moi_mua_giong_het)
# Xem địa chỉ trong bộ nhớ (ID)
print("id(xe_cua_ban) : ", id(xe_cua_ban))
print("id(xe_ban_muon): ", id(xe_ban_muon))
print("id(xe_moi_mua_giong_het) : ", id(xe_moi_mua_giong_het))


# Toán tử is not
# Toán tử is not trong Python được dùng để kiểm tra xem hai đối tượng có khác biệt về vị trí trên bộ nhớ hay không.
# Kết quả của phép so sánh is not là True nếu hai đối tượng không cùng nằm trên một ô nhớ, và False nếu ngược lại.

# Để dễ hình dung, hãy tưởng tượng bạn có hai cuốn sổ tay:
so_tay_cua_An = ["Việc A", "Việc B", "Việc C"]  # An có một cuốn sổ tay
so_tay_cua_Binh = ["Việc A", "Việc B", "Việc C"]  # Bình cũng có một cuốn sổ tay
so_tay_cua_An_Ban_Sao = so_tay_cua_An # An tạo một bản sao của số tay của bạn

# So sánh
print("Sổ tay của An có khác sổ tay An bản sao không? ", so_tay_cua_An is not so_tay_cua_An_Ban_Sao)
print("Sổ tay của An có khác sổ tay của Bình không? ", so_tay_cua_An is not so_tay_cua_Binh)

# Xem vị trí trên bộ nhớ (bạn không cần nhớ các con số này, chỉ cần quan sát sự giống/khác nhau)
print("Vị trí sổ tay An:", id(so_tay_cua_An))
print("Vị trí sổ tay Bình:", id(so_tay_cua_Binh))
print("Vị trí bản sao sổ tay An:", id(so_tay_cua_An_Ban_Sao))