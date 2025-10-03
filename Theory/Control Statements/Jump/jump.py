# Lệnh break
# Lệnh break sẽ kết thúc vòng lặp hiện tại và chương trình tiếp tục thực thi ở câu lệnh kế tiếp sau vòng lặp đó.
x = 0

while x < 10:
    print("x:", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1

print("End")

# Lệnh continue
# Lệnh continue sẽ bỏ qua phần còn lại của khối lệnh bên trong vòng lặp 
# và chuyển quyền điều khiển trở lại đầu vòng lặp hiện tại để bắt đầu lần lặp tiếp theo
for letter in "Python":
    # continue when letter is 'h'
    if letter == "h":
        continue
    print("Current Letter :", letter)