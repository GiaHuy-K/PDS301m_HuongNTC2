import os
# help(os)
print("Current directory: ",os.getcwd())

# os.chdir("C:\\Users\\Admin\\Desktop\\PDS301m_HuongNTC2\\PDS301m_HuongNTC2-\\Lesson\\Day26.9.2025")
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day26.9.2025")
print("Check directory", os.getcwd())

file = open("TextFile.txt","w")
file.write("FPT University\n")
file.write("Ho Chi Minh\n")
file.write("Nha Van Hoa Dh QG\n")
file.close()

file = open("TextFile.txt")
print(file.read())

file = open("TextFile.txt","a")
file.write("He he he\n")
file.close()

