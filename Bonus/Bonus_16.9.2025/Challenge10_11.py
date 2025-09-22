# 10. Create a list containing the titles of four TV programmes and display them on separate lines. Ask the
# user to enter another show and a position they want it inserted into the list. Display the list again,
# showing all five TV programmes in their new positions. 
# TV_programmes = ["Hello", "Hi", "How are you", "I'm fine"]
# print("List of TV programmes: ")
# for idx, show in enumerate(TV_programmes, start=1):
#     print(f"{idx}. {show}")

# Name = input("Enter another show: ")
# pos = int(input("Enter position that u wanna add your show in the list above: "))

# TV_programmes.insert(pos - 1, Name) 
# print("List of TV programmes: ")
# for idx, show in enumerate(TV_programmes, start=1):
#     print(f"{idx}. {show}")

# 11. Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add
# it to the end of the nums list and display the list. Once they have entered three numbers, ask them if
# they still want the last number they entered saved. If they say “no”, remove the last item from the list.
# Display the list of numbers.
nums = []
for i in range(3):
    x = int(input("Enter the number:"))
    nums.append(x)
    if i == 2:
        while True:
            choose = input("Do you want to keep the last number? (Y/N): ").lower()
            if choose == "n":
                nums.pop()   # xóa phần tử cuối cùng
                break
            elif choose == "y":
                break
            else:
                print("Please enter Y or N.")
print("The list of number:", nums)