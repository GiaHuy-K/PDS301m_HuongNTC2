# Họ Và Tên: Khổng Trần Gia Huy
# MSSV: SE180313

# Q1:
# A: 90 – 100
# B: 80 – 89
# C: 70 – 79
# D: 60 – 69
# F: below 60
print("============================ Q1 ============================")
score_input = int(input("Enter the student's score:"))
if score_input < 60 :
    print("F")
elif score_input >= 60 and score_input <= 69 :
    print("D")
elif score_input >= 70 and score_input <= 79 :
    print("C")
elif score_input >= 80 and score_input <= 89 :
    print("B")
elif score_input >= 90 and score_input <= 100 :
    print("A")
    
# Q2: Supermarket Bill Calculator (for loop)
# A supermarket cashier scans the prices of items in a shopping cart.
# Write a program that uses a for loop to calculate the total bill.
# Requirement: The cashier enters the prices of n items. The program should display the total amount.
print("============================ Q2 ============================")
items_input = int(input("Enter the amount of item that you wanna calculate:"))
total = 0
for i in range(items_input):
    item_price = float(input(f"Enter the prices of {i+1} item: "))
    total  += item_price
print(f"The total of {items_input} item is: {total}")

# Q3: Bus Ticket Purchase (while loop)
# A person buys bus tickets until they run out of money. Each ticket costs 15 VND.
# Requirement: Start with an initial balance.
# Use a while loop to simulate buying tickets until balance is insufficient. 
# Display how many tickets were bought and the remaining balance.
print("============================ Q3 ============================")
balance = int(input("Enter your initial balance: VND "))
ticket_price = 15
ticket_total = 0

while balance >= ticket_price:
    balance -= ticket_price
    ticket_total += 1
print(f"You have bought {ticket_total} bus tickets.")
print(f"Your remain balance: {balance} VND")


# Q4: Create a program that will allow the user to easily manage a list of names. 
# You should display a menu that will allow them to 1)add a name to the list,
# 2)change a name in thelist, 3)delete a name from the list or 4)view all the names in the list. 
# 5)There should also be a menu option to allow the user to end the program. 
# 6)If they select an option that is not relevant, then it should display a suitable message. 
# 7)After they have made a selection to either add a name, change a name, delete a name or view all the names, 
# they should see the menu again without having to restart the program. The program should be made as easy to use as possible.

# Viết các function và gọi trong main : # def add_name() ; #def change_name(); # def delete_name(); #def view_name(); #def main().
print("============================ Q4 ============================")
names = []

# add C
def add_name():
    name = input("Enter the name u wanna add: ")
    names.append(name)
    print(f"{name} has been added.")
    
# view R
def view_names():
    if not names:
        print("The list is empty.")
    else:
        print("Current names in the list:")
        for i, name in enumerate(names, start=1):
            print(f"{i}. {name}")
            
# change U
def change_name():
    if not names:
        print("The list is empty. Nothing to change.")
        return
    view_names()
    try:
        index = int(input("Enter the number of the name you want to change: ")) - 1
        if 0 <= index < len(names):
            new_name = input("Enter the new name: ")
            old_name = names[index]
            names[index] = new_name
            print(f"{old_name} has been changed to {new_name}.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
        
# delete D
def delete_name():
    if not names:
        print("The list is empty. Nothing to delete.")
        return
    view_names()
    try:
        index = int(input("Enter the number of the name you want to delete: ")) - 1
        if 0 <= index < len(names):
            removed = names.pop(index)
            print(f"{removed} has been deleted.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

# main  
def main():
    while True:
        print("\n===================== Menu =====================")
        print("1. Add a name")
        print("2. Change a name")
        print("3. Delete a name")
        print("4. View all names")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_name()
        elif choice == "2":
            change_name()
        elif choice == "3":
            delete_name()
        elif choice == "4":
            view_names()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    main()