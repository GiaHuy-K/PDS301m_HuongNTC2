# 7. Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line. 
# Ask the user to enter a three-digit number. 
# If the number they have typed in matches one in the list, display the position of that number in the list, 
# otherwise display the message “That is not in the list”. 
# Numbers = [100, 200, 300, 400]
# print("List of numbers:")
# for i in range(len(Numbers)):
#     print(Numbers[i])
# x = int(input("Enter a three-digit number:"))
# if x in Numbers:
#     pos = Numbers.index(x)
#     print("Position of ur number is:",pos)
# else:
#     print("That is not in the list")



# 8. Ask the user to enter the names of three people they want to invite to a party and store them in a list. 
# After they have entered all three names, ask them if they want to add another. 
# If they do, allow them to add more names until they answer “no”. 
# When they answer “no”, display how many people they have invited to the party.
# Invited = []

# # nhập 3 người đầu tiên
# for i in range(3):
#     name = input(f"Enter name {i+1}: ")
#     Invited.append(name)

# # hỏi có muốn thêm không
# while True:
#     aMore = input("Do you wanna add more (yes/no): ").lower()
#     if aMore == "yes":
#         name = input("Enter another name: ")
#         Invited.append(name)
#     elif aMore == "no":
#         break
#     else:
#         print("Please answer yes or no.")

# print("You have invited", len(Invited), "people to the party.")


                

# 9. Change program 08 so that once the user has completed their list of names, display the
# full list and ask them to type in one of the names on the list. Display the position of that
# name in the list. Ask the user if they still want that person to come to the party. If they
# answer “no”, delete that entry from the list and display the list again. 
Invited = []

# nhập 3 người đầu tiên
for i in range(3):
    name = input(f"Enter name {i+1}: ").strip()
    Invited.append(name)
print("Your invite list:",Invited)
while True:
    choose_name = input("Enter name in above list:").strip()
    if choose_name in Invited:
        break
    else:
        print("Name not in the list!!! Please enter again.")
pos = Invited.index(choose_name)
print("The position of that name in the list is: ", pos)
YN = input("Do you still want this person come to the party?(Y/N)").lower()
if YN == "n":
    # Invited.remove(choose_name)
    # cách 2 xóa theo index
    del Invited[pos]
print("The list after u remove that person", Invited)