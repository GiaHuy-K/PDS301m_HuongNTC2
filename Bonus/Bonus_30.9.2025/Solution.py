# Bài tập thêm: 
# If the user selects 1, allow them to add to a file called Salaries.csv which will store their name and salary. 
# If they select 2 it should display all records in the Salaries.csv file. 
# If they select 3 it should stop the program. If they select an incorrect option they should see an error message.
# They should keep returning to the menu until they select option 3.
# 4.In Python, it is not technically possible to directly delete a record from a .csv file. 
# Instead you need to save the file to a temporary list in Python,
# make the changes to the list and then overwrite the original file with the temporary list. 
# Change the previous program to allow you to do this. Your menu should now look like this:

# 1) Add to file
# 2) View all records
# 3) Delete a record
# 4) Quit the program

# Enter the number of your selection:
import os
import csv
print("Check directory:", os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Bonus\Bonus_30.9.2025")
print("Current directory:", os.getcwd())

# add
def add_file():
    name = input("Enter name: ")
    salary = input("Enter salary: ")
    with open("Salaries.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, salary])
# display 
def display_file():
    try:
        with open("Salaries.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found. Please add data first.")
        
# main
def main():
    while True:
        print("\n===================== Menu =====================")
        print("1. Add to file")
        print("2. View all records")
        print("3. Quit the program")

        choice = input("Enter the number of your selection: ")

        if choice == "1":
            add_file()
        elif choice == "2":
            display_file()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select from 1-3.")




if __name__ == "__main__":
    main()
#TODO: CÒN PHẦN XÓA RECORD