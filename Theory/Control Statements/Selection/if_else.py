# Nếu phần thân của một mệnh đề if chỉ có một dòng lệnh duy nhất, 
# bạn có thể viết nó trên cùng một dòng với phần tiêu đề if.
var = 100
if ( var == 100 ) : print ("Giá trị của biến là 100")
print ("Tạm biệt!")

# if..elif..else
marks = 80
result = ""
if marks < 30:
    result = "Failed"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)
# nested if
var = 100
if ( var == 100 ):
   print("Số này bằng 100")
   if var % 2 == 0:
      print("Số này là số chẵn")
   else:
      print("Số này là số lẻ")
elif var == 0:
   print("Số này bằng 0")
else:
   print("Số này là số âm")

