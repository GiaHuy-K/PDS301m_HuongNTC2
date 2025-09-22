# 4. Create a list of six school subjects. Ask the user which of these subjects they don’t like. 
# Delete the subject they have chosen from the list before you display the list again.
Subjects = ["Math","Biology","Physics","History","Chemistry","Geography"]
print("List of subjects:",Subjects)

x = input("Enter subject that u dislike: ")
if x in Subjects:
    Subjects.remove(x)   
    print("Updated list:", Subjects)
else:
    print("Not found")

# 5. Ask the user to enter four of their favorite foods and store them in a dictionary so that they are indexed with numbers starting from 1.
# Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list. 
# Sort the remaining data and display the dictionary.
Foods = {}
for i in range(1, 5):   
    food = input(f"Enter favourite food {i}: ")
    Foods[i] = food

print("Your foods:", Foods)
# remove
remove_idx = int(input("Which food do you wanna remove (Enter index)? :"))

if remove_idx in Foods:
    del Foods[remove_idx]
sorted_foods = dict(sorted(Foods.items(), key=lambda item: item[1]))

print("Updated and sorted foods:", sorted_foods)

    
# 6. Enter a list of ten colors. Ask the user for a starting number between 0 and 4 and an end number
# between 5 and 9. Display the list for those colors between the start and end numbers the user input. 
Colors = ["Green", "Yellow", "Blue", "Purple", "Pink", 
          "Black", "White", "Grey", "Orange", "Violet"]

# nhập start
while True:
    snum = int(input("Enter start number (0 - 4): "))
    if 0 <= snum <= 4:
        break
    print("Invalid. Must be between 0 and 4.")

# nhập end
while True:
    enum = int(input("Enter end number (5 - 9): "))
    if 5 <= enum <= 9 and enum > snum:
        break
    print("Invalid. Must be between 5 and 9 and greater than start.")

print("The list u wanna see:", Colors[snum:enum])