# 1. Câu lệnh match trong Python (switch case trong java hoặc C/C++)
def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
      
user_input= int(input("Enter 0-6:"))
print (weekday(user_input))


# test thử tí về phân quyền nào 
def access(user):
   match user:
      case "admin" | "manager": return "Full access"
      case "Guest": return "Limited access"
      case _: return "No access"
print (access("manager"))
print (access("Guest"))
print (access("Bo"))

# 2. Sử dụng danh sách (List) làm đối số trong câu lệnh match-case
# Vì Python có thể so khớp biểu thức với bất kỳ giá trị nào (literal), bạn có thể dùng một danh sách làm giá trị của case.
# Hơn nữa, đối với danh sách có số lượng phần tử thay đổi, bạn có thể sử dụng toán tử * để phân tách các phần tử thành một chuỗi.
def greeting(details):
   match details:
      case [time, name]:
         return f'Good {time} {name}!'
      case [time, *names]:
         msg=''
         for name in names:
            msg+=f'Good {time} {name}!\n'
         return msg

print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))

# thêm tí if cho nó zui bae
def intr(details):
   match details:
      case [amt, duration] if amt<10000:
         return amt*10*duration/100
      case [amt, duration] if amt>=10000:
         return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))