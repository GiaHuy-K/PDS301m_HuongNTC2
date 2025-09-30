import csv
import os
# help(os)
print("Current directory: ",os.getcwd())

# os.chdir("C:\\Users\\Admin\\Desktop\\PDS301m_HuongNTC2\\PDS301m_HuongNTC2-\\Lesson\\Day26.9.2025")
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day26.9.2025")
print("Check directory", os.getcwd())

# dữ liệu cần lưu
books = [
    ["Book", "Author", "Year Released"],
    ["To Kill A Mockingbird", "Harper Lee", 1960],
    ["A Brief History of Time", "Stephen Hawking", 1988],
    ["The Great Gatsby", "F. Scott Fitzgerald", 1922],
    ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", 1985],
    ["Pride and Prejudice", "Jane Austen", 1813]
]

# tạo file Books.csv và ghi dữ liệu
with open("Books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(books)
# đọc file Books.csv
with open("Books.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

   
print("Books.csv has been created.")
# 2 thêm một cuốn sách mới
name_book = input("Enter new book name:")
author_book = input("Enter author name:")
year_book = input("Enter year Released:")
new_book = [name_book,author_book,year_book]
with open("Books.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_book)
# đọc file Books.csv
with open("Books.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 

# Bai 3- csv: Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many.
# After all the data has been added, ask for an author and display all the books in the list by that author. 
# If there are no books by that author in the list, display asuitable message.

choice = int(input("Enter the number of book u wanna add:"))
for i in range(choice):
    print(f"The {i+1} book:\n")
    name_book = input("Enter new book name:")
    author_book = input("Enter author name:")
    year_book = input("Enter year Released:")
    new_book = [name_book,author_book,year_book]
    with open("Books.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_book)

# đọc file Books.csv
with open("Books.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Bai 4- csv: Using the Books.csv file, ask the user to enter a starting year and an end year.
# Display all books released between those two years.

# Bai 5- csv: Using the Books.csv file, display the data in the file along with the row number of each.
# Bai 6- csv: Import the data from the Books.csv file into a list. Display the list to the user. 
# Ask them to select which row from the list they want to delete and remove it from the list. 
# Ask the user which data they want to change and allow them to change it.
# Write the data back to the original .csv file, overwriting the existing data with the amended data.

# Bai 7- Create a simple maths quiz that will ask the user for their name and then generate two random questions.
# Store their name, the questions they were asked, their answers and their final score in a .csv file.
# Whenever the program is run it should add to the .csv file and not overwrite anything.