# Scenario: You would like to create a series of hillshade rasters to represent summer, winter and equinox
# conditions. The hillshade tool requires inputs of sun angle (the sun's maximum altitude in the sky on a given
# day) and azimuth. The sun angle depends on the solar declination. You could look up values in a table, but why
# not have the computer derive these from what you know? We'll start with a somewhat informed situation -- we
# know the values for solar declination for four significant dates during the year:
# ⌨ Enter the following code that derives sun angle and azimuth from solar declination (the latitude where the
# sun's rays are vertical at noon) and latitude. It starts with information to populate two variables, lat (latitude for
# the area of study, negative if south of the equator) and decl (solar declination), and from these derives
# sunangle and azimuth :
lat = 30
decl = 20
sunangle = 90 - lat + decl
azimuth = 180
if sunangle > 90:
    sunangle = 180 - sunangle
    azimuth = 0
print(f"Noon sun angle {sunangle}, at azimuth {azimuth}")

# For now, we've hard-coded the inputs of lat and decl . In this case sunangle would be assigned the value
# 80 since 90 - 30 + 20 is evaluated as 80. The next line assigns 180 to the variable azimuth . There's then a
# section of statements that assigns new values to sunangle and azimuth if sunangle ends up with value
# greater than 90 after the first two lines are processed. Sun azimuth is either from the south (180) or from the
# north (0) at solar noon.
# Note the formatting of the if structure:
# starts with if followed by a Boolean expression ( sunangle > 90 ) as a condition followed by a colon :
# the code that will run if the condition is true follows as an indented series of statements
# the next indented code continues the program code: it runs whether or not the if structure runs (as long as
# there's no error raised)
print('\n\nStart of script...')
x = 5
if x > 0:
    print('In the "if" block, since x > 0 ...')
    print('Still in the indented "if" block ...')
print("Not indented -- we're at the next step in the script.")

print("\n ")
print("Using if with files and folders ...")
# Có hai cách để làm việc với file path

# Cách 1: dùng đường dẫn tuyệt đối (absolute path)
# Đường dẫn tuyệt đối là đường dẫn đầy đủ từ ổ đĩa gốc (C:/, D:/...) đến file hoặc folder

import os.path
if os.path.exists("C:\\Users\\Admin\\Desktop\\PDS301m_HuongNTC2\\PDS301m_HuongNTC2-\\Basic\\Exercise2\\2.2.Flow Control Structures\\data"):
    print("data folder exists")
    
# cách 2: dùng đường dẫn tương đối (relative path)
# đường dẫn tương đối là đường dẫn tính từ thư mục hiện hành (current working directory)
print("Current working directory:", os.getcwd()) # check thử đường dẫn và in ra thư mục hiện hành

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Đổi current working directory (cwd) về đúng thư mục chứa file .py đang chạy
# os.path.abspath(__file__) → lấy đường dẫn tuyệt đối của file Python hiện tại.
# os.path.dirname(...) → lấy folder chứa file đó.
# os.chdir(...) → đổi cwd về folder đó, để khi mình dùng "data" thì nó tìm ngay trong cùng chỗ chứa file .py.

print("Current working directory:", os.getcwd())

# Đường dẫn thư mục và file
data_folder = "data"
data_file = os.path.join(data_folder, "data.txt")

if os.path.exists(data_file):
    print("Data folder exists.")
    print("Text file exists.")
elif os.path.exists(data_folder):
    print("Data folder exists.")
    print("... but text file doesn't.")
else:
    print("Neither exist.")
