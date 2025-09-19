# Toán tử số học là toán tử hai ngôi (binary operator) có nghĩa là nó cần 2 toán hạng(operand) để thực hiện phép toán.
# Toán tử số học trong Python bao gồm: +, -, *, /, %, **, //

print("1. Toán tử cộng (+):")
a = 25
b = 12
print ("Phép cộng hai số nguyên")
print ("a =", a, "b =", b, "tổng =", a + b)
a = 30
b = 7.5
print ("Phép cộng số nguyên và số thực")
print ("a =", a, "b =", b, "tổng =", a + b)
a = 15 +8j
b = 6.2
print ("Phép cộng số phức và số thực")
print ("a =", a, "b =", b, "tổng =", a + b)

print("--------------------------------\n")
print("2. Toán tử trừ (-):")
a = 25
b = 10
print ("Phép trừ hai số nguyên")
print ("a = ", a, "b =", b, "a - b =", a - b)
print ("a =" , a, "b =", b, "b - a =", b - a)
a = 15
b = 25.5 
print(" Phép trừ giữa số nguyên và số thực:")
print("a =",a,"b =",b, "a - b =", a - b)
print("a =", a, "b =", b, "b - a =", b - a)

a = 12 + 4j
b = 15.5
print("Phép trừ giữa số phức và số thực:")
print("a =", a, "b =", b, "a - b =", a - b)
print("a =", a, "b =", b, "b - a =", b - a)

print("--------------------------------\n")
print("3. Toán tử nhân (*):")
a = 10
b = 20
print("Phép nhân hai số nguyên:")
print("a =", a, "b =", b, "a * b =", a * b)
a = 10
b = 20.5
print("Phép nhân số nguyên và số thực:")
print("a =", a, "b =", b, "a * b =", a * b)

a = -5.55
b = 6.75E-3
print("Phép nhân hai số thực:")
print("a =", a, "b =", b, "a * b =", a * b)
a = 10 + 5j
b = 20.5
print("Phép nhân số phức và số thực:")
print("a =", a, "b =", b, "a * b =", a * b)

print("--------------------------------\n")
print("4. Toán tử chia (/):")
a = 15
b = 3
print ("Phép chia hai số nguyên:")
print ("a =", a, ", b =", b, ", a / b =", a / b)
print ("a =", a, ", b =", b, ", b / a =", b / a)
a = 10
b = -5.5
print ("Phép chia số nguyên và số thực:")
print ("a =", a, ", b =", b, ", a / b =", a / b)
a = -7.5
b = 1.5e2 #tương ứng 1.5 * 10^2 = 150
print ("Phép chia giữa hai số thực:")
print ("a =", a, ", b =", b, ", a / b =", a / b)
a = 3 + 6j  # Số phức
b = 1.5    # Số thực
print ("Phép chia giữa số phức và số thực:")
print ("a =", a, ", b =", b, ", a / b =", a / b)
print ("a =", a, ", b =", b, ", b / a =", b / a)

print("--------------------------------\n")
print("5. Toán tử chia lấy dư (%):")
a = 10
b = 2
print ("a =", a, "b =", b, "a%b =", a % b) # 10 chia 2 dư 0
a = 10
b = 4
print ("a =", a, "b =", b, "a%b =", a % b) # 10 chia 4 dư 2
print ("a =", a, "b =", b, "b%a =", b % a) # 4 chia 10 dư 4 (số bị chia < số chia)
a = 0
b = 10
print ("a =", a, "b =", b, "a%b =", a % b) # 0 chia 10 dư 0

try:
    print ("a=", a, "b=", b, "b%a=",b%a)  # 10 chia 0 sẽ gây lỗi
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
 
a = 10
b = 2.5
print ("a =", a, "b =", b, "a%b =", a % b) # 10 chia 2.5 dư 0.0
a = 10
b = 1.5
print ("a =", a, "b =", b, "a%b =", a % b) # 10 chia 1.5 dư 1.0
a = 7.7
b = 2.5
print ("a =", a, "b =", b, "a%b =", a % b) # 7.7 chia 2.5 dư 0.200000...
a = 12.4
b = 3
print ("a =", a, "b =", b, "a%b =", a % b)  # 12.4 chia 3 dư 0.400000...   

print("--------------------------------\n")
print("6. Toán tử lũy thừa (**):")
co_so = 5
so_mu = 2
print (f"{co_so} mũ {so_mu} bằng: {co_so**so_mu}") # 5 mũ 2 = 25

co_so = 3
so_mu = 1.5
print (f"{co_so} mũ {so_mu} bằng: {co_so**so_mu}") # 3 mũ 1.5 ~ 5.196

co_so = 2.5
so_mu = 3
print (f"{co_so} mũ {so_mu} bằng: {co_so**so_mu}") # 2.5 mũ 3 = 15.625

co_so = 2+1j #Số phức
so_mu = 2
print (f"{co_so} mũ {so_mu} bằng: {co_so**so_mu}") # (2+1j) mũ 2 = 3+4j
co_so = 7
so_mu = 0
print (f"{co_so} mũ {so_mu} bằng: {co_so**so_mu}") # 7 mũ 0 = 1

print("--------------------------------\n")
print("7. Toán tử chia lấy nguyên (//):")
a = 9
b = 2
print("a =", a, "b =", b, "a//b =", a // b) # 9 chia nguyên cho 2

a = 9
b = -2
print("a =", a, "b =", b, "a//b =", a // b) # 9 chia nguyên cho -2

a = 10
b = 1.5
print("a =", a, "b =", b, "a//b =", a // b) # 10 chia nguyên cho 1.5

a = -10
b = 1.5
print("a =", a, "b =", b, "a//b =", a // b) # -10 chia nguyên cho 1.5