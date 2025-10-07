# 1. Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines. 
# Once you have run the program, look in the location where your program is stored and check that the file has been created properly. 
# Display the list of names in Python. 
# Ask the user to type in one of the names and then save all the names except the one they entered into a new file called Names2.txt.
# # ==========================================================
# import os
# # check Đường dẫn
# print("Current directory:",os.getcwd())

# os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day26.9.2025\Exercise")
# print("\nCheck directory:",os.getcwd())

# # tạo file mới và lưu 5 tên vào file 
# file = open("Names.txt","w")
# file.write("Hong\n")
# file.write("Hao\n")
# file.write("Linh\n")
# file.write("Luc\n")
# file.write("Le\n")
# file.close()

# # Ghi nội dung file ra và lưu vào một biến
# file = open("Names.txt")
# print(file.read())
# file.close()
# file = open("Names.txt")

# names = file.readlines()
# print(names)
# file.close()
# # remove name trong danh sách
# remove_name = input("Enter name that you dislike in the list:").strip()

# file = open("Names2.txt","w")
# for i in names:
#     if i.strip() != remove_name:   
#         file.write(i)
# file.close()
# # =====================================================================================


# 2.  Display the following menu to the user: 
#      1) Create a new file
#      2) Display the file
#      3) Add a new item to the file.
#    Make a selection 1, 2, or 3:
#     - Ask the user to enter 1, 2 or 3.   
# If they select anything other than 1, 2 or 3 it should display a suitable error message.
# If they select 1, ask the user to enter a school subject and save it to a new file called “Subject.txt”.
# It should overwrite any existing file with a new file.
# If they select 2, display the contents of the “Subject.txt” file.
# If they select 3, ask the user to enter a new subject and save it to the file and then display the entire contents of the file.
# Run the program several times to test the options.

import os
# check Đường dẫn
print("Current directory:",os.getcwd())

os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day26.9.2025\Exercise")
print("\nCheck directory:",os.getcwd())



while True:
    print("\n")
    print("0) Exit the program")
    print("1) Create a new file")
    print("2) Display the file")
    print("3) Add a new item to the file")
    user_input = input("Enter your choose(1-3 or 0 to exit):")
    if user_input == '1':
        school = input("Enter school subject: ")
        file = open("Subject.txt","w")
        file.write(school)
        file.close()
        print("New file created.")
    elif user_input == '2':
        file = open("Subject.txt")
        print(file.read())
        file.close()
    elif user_input == '3':
        school = input("Enter new school subject: ")
        file = open("Subject.txt","a")
        file.write(school)
        file.close()
    else:
        print("Please choose 1-3")



