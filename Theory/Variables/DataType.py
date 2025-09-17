# Kiểu dữ liệu	    Ví dụ
# Numeric	        int (số nguyên), float (số thực), complex (số phức)
# String	        str (chuỗi kí tự)
# Sequence	        list (danh sách), tuple (bộ), range (phạm vi)
# Binary	        bytes, bytearray (mảng byte), memoryview
# Mapping	        dict (từ điển)
# Boolean	        bool (giá trị True/False)
# Set	            set, frozenset
# None	            NoneType

# Điểm khác biệt chính giữa list và tuple là: List được đặt trong dấu ngoặc vuông [ ], 
# các phần tử và kích thước của list có thể thay đổi (list có thể thay đổi – mutable). 
# Trong khi đó, tuple được đặt trong dấu ngoặc đơn ( ) và không thể thay đổi sau khi đã tạo (tuple bất biến – immutable). 
# Bạn có thể xem tuple như một danh sách “chỉ đọc”.

print("Các kiểu dữ liệu số trong python ")
var1 = 1        # Kiểu dữ liệu số nguyên (int)
var2 = True     # Kiểu dữ liệu boolean (bool)
var3 = 10.023   # Kiểu dữ liệu số thực (float)
var4 = 10+3j    # Kiểu dữ liệu số phức (complex)
# biến số nguyên.
a = 100
print("Kiểu của biến có giá trị", a, " là ", type(a))

# biến số thực.
c = 20.345
print("Kiểu của biến có giá trị", c, " là ", type(c))

# biến số phức.
d = 10 + 3j
print("Kiểu của biến có giá trị", d, " là ", type(d))

# Kiểu dữ liệu chuỗi trong Python
# Trong Python, chuỗi (string) là một dãy các ký tự Unicode, có thể chứa một hoặc nhiều ký tự. 
# Các chuỗi này được đặt trong dấu nháy đơn ('),dấu nháy kép ("), hoặc dấu nháy ba (''' hoặc """). 
# Các chuỗi trong Python là bất biến (immutable), 
# có nghĩa là khi bạn thực hiện một thao tác trên chuỗi, một đối tượng chuỗi mới sẽ được tạo ra thay vì chỉnh sửa trực tiếp chuỗi gốc.
print("Ví dụ về kiểu dữ liệu chuỗi trong Python")
str = 'Xin chào mọi người!'

print (str)        # In ra toàn bộ chuỗi
print (str[0])     # In ra ký tự đầu tiên của chuỗi
print (str[2:5])   # In ra các ký tự từ vị trí thứ 3 đến vị trí thứ 5 (không bao gồm vị trí thứ 5)
print (str[2:])    # In ra chuỗi bắt đầu từ ký tự thứ 3
print (str * 2)    # In ra chuỗi lặp lại 2 lần
print (str + " (Test)")  # In ra chuỗi đã được ghép

# Các kiểu dữ liệu sequence trong Python
# Sequence là một kiểu dữ liệu tập hợp. Các Sequence cho phép chứa các phần tử theo một thứ tự nhất định. 
# Các phần tử trong sequence có một chỉ mục vị trí, bắt đầu từ 0. Về mặt khái niệm, nó tương tự như mảng (array) trong C hoặc C++. 
# Có ba kiểu dữ liệu sequence chính được định nghĩa trong Python:

# Kiểu dữ liệu Danh Sách (List)
# Kiểu dữ liệu Bộ (Tuple)
# Kiểu dữ liệu Dải Số (Range)
# Các sequence trong Python là iterable và có giới hạn – 
# Khi chúng ta nói đến một iterable trong Python, nó thường đề cập đến một kiểu dữ liệu sequence (ví dụ, danh sách).
print("Ví dụ về kiểu dữ liệu danh sách (list) trong Python")
list = [ 'Vietnix', 521 , 2.24, 'Cry', 26.2 ]
tinylist = [123, 'Bo']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

print("Ví dụ về kiểu dữ liệu bộ (tuple) trong Python")
tuple = ( 'Vietnix', 524 , 2.24, 'Bo', 64.2  )
tinytuple = (123, 'happy')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples
# Kiểu dữ liệu range trong Python
# Trong Python, range là một dãy số bất biến, thường được dùng để lặp qua một số lượng phần tử nhất định.
#
# range được biểu diễn bởi lớp (class) Range. Hàm khởi tạo (constructor) của lớp này chấp nhận một dãy số, 
# bắt đầu từ 0 và tăng dần lên 1 cho đến khi đạt đến một số được chỉ định. Cú pháp của hàm range như sau:
# range(start, stop, step)
# Dưới đây là mô tả chi tiết các tham số được sử dụng:

# start: Số nguyên chỉ định vị trí bắt đầu (tùy chọn, mặc định là 0).
# stop: Số nguyên chỉ định vị trí kết thúc (bắt buộc).
# step: Số nguyên chỉ định bước nhảy (tùy chọn, mặc định là 1)
print("Kiểu dữ liệu byte trong python ")
# Kiểu dữ liệu bytes trong Python
# Kiểu dữ liệu bytes trong Python biểu diễn một chuỗi các byte.
# Mỗi byte là một giá trị số nguyên nằm trong khoảng từ 0 đến 255. 
# Nó thường được dùng để lưu trữ dữ liệu nhị phân, như hình ảnh, tập tin hoặc các gói dữ liệu mạng.
# Chúng ta có thể tạo bytes trong Python bằng cách sử dụng hàm bytes() dựng sẵn hoặc bằng cách thêm tiền tố b vào trước một chuỗi số.
# Sử dụng hàm bytes() để tạo bytes
b1 = bytes([65, 66, 67, 68, 69])
print(b1)

print("Ví dụ về kiểu dữ liệu bytearray trong Python")
# Kiểu dữ liệu bytearray trong Python
# Kiểu dữ liệu bytearray trong Python khá giống với kiểu bytes, 
# nhưng có một điểm khác biệt quan trọng: bytearray có thể thay đổi (mutable). 
# Điều này nghĩa là bạn có thể chỉnh sửa các giá trị được lưu trữ trong nó sau khi bytearray đã được tạo ra.
# Bạn có thể tạo một bytearray bằng nhiều cách khác nhau, 
# bao gồm việc truyền vào một chuỗi các số nguyên (iterable of integers) biểu diễn giá trị byte, 
# bằng cách mã hóa một chuỗi, hoặc bằng cách chuyển đổi một đối tượng bytes hoặc bytearray có sẵn. 
# Để thực hiện việc này, chúng ta sử dụng hàm bytearray().
# Tạo một bytearray từ một chuỗi số nguyên
value = bytearray([72, 101, 108, 108, 111])
print(value)
# Tạo một bytearray bằng cách mã hóa một chuỗi
val = bytearray("Hello", 'utf-8')
print(val)

# Kiểu dữ liệu memoryview trong Python
# Trong Python, memoryview là một đối tượng tích hợp sẵn, cung cấp một “cái nhìn” (view) vào vùng nhớ của một đối tượng gốc. 
# Các đối tượng này thường hỗ trợ giao thức buffer, ví dụ như mảng byte (bytearray) và byte (bytes). 
# memoryview cho phép bạn truy cập vào dữ liệu bên dưới của đối tượng gốc mà không cần sao chép nó. 
# Điều này giúp truy cập bộ nhớ một cách hiệu quả, đặc biệt với các tập dữ liệu lớn.

# Bạn có thể tạo một memoryview bằng nhiều cách, ví dụ như sử dụng hàm khởi tạo memoryview(), 
# sử dụng thao tác cắt (slicing) trên các đối tượng bytes hoặc bytearray, trích xuất từ các đối tượng array,
# hoặc sử dụng các hàm tích hợp sẵn như open() khi đọc từ file.
print("ví dụ về kiểu dữ liệu memoryview trong Python")
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)


# Kiểu dữ liệu dictionary trong Python
# Dictionary (từ điển) trong Python là một dạng bảng băm (hash table). 
# Khóa (key) của từ điển có thể là hầu hết các kiểu dữ liệu trong Python, nhưng thường là số hoặc chuỗi. 
# Mặt khác, giá trị (value) có thể là bất kỳ đối tượng Python nào.

# Dictionary trong Python giống như mảng kết hợp (associative arrays) hay hash trong Perl. 
# Dictionary chứa các cặp key:value, các cặp này được phân tách bằng dấu phẩy và được đặt trong cặp ngoặc nhọn {}. 
# Để liên kết giữa khóa và giá trị, ta dùng dấu hai chấm (:) giữa chúng.
print("Ví dụ về kiểu dữ liệu dictionary trong Python")
dict = {}
dict['one'] = "Đây là một"
dict[2] = "Đây là hai"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # In ra giá trị tương ứng với khóa 'one'
print (dict[2])           # In ra giá trị tương ứng với khóa 2
print (tinydict)          # In ra toàn bộ từ điển tinydict
print (tinydict.keys())   # In ra danh sách các khóa của tinydict
print (tinydict.values()) # In ra danh sách các giá trị của tinydict

# Kiểu dữ liệu set trong Python
# Trong Python, set (tập hợp) là một cách triển khai khái niệm tập hợp trong toán học. 
# Set là một dạng tập hợp các phần tử, nhưng nó không phải là một tập hợp có thứ tự hay đánh số chỉ mục như string (chuỗi), 
# list (danh sách) hay tuple (bộ). Một đối tượng không thể xuất hiện nhiều hơn một lần trong một set,
# trong khi ở list và tuple thì các đối tượng có thể xuất hiện nhiều lần.

# Các phần tử trong set được phân tách bằng dấu phẩy và được đặt bên trong dấu ngoặc nhọn {}. 
# Các phần tử của một set có thể thuộc các kiểu dữ liệu khác nhau.

#  Lưu ý: Các phần tử trong một set có thể không theo cùng thứ tự mà bạn nhập vào.
# Vị trí của các phần tử được Python tối ưu hóa để thực hiện các thao tác trên tập hợp như định nghĩa trong toán học.
set1 = {123, 452, 5, 6}
set2 = {'Java', 'Python', 'JavaScript'}

print(set1)
print(set2)

# Kiểu dữ liệu boolean trong Python
# Kiểu dữ liệu Boolean là một trong các kiểu dữ liệu cơ bản của Python, 
# biểu diễn một trong hai giá trị: True (Đúng) hoặc False (Sai). 
# Hàm bool() trong Python cho phép bạn đánh giá giá trị của bất kỳ biểu thức nào và trả về True hoặc False dựa trên kết quả của biểu thức đó.

# Một biến Boolean chỉ có hai giá trị khả thi, được thể hiện bằng các từ khóa True và False. Chúng tương ứng với số nguyên 1 và 0.
print("Ví dụ về kiểu dữ liệu boolean trong Python")
a = True
# hiển thị giá trị của a
print(a)

# hiển thị kiểu dữ liệu của a
print(type(a))