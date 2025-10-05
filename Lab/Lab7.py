# Exercise 1:
print("Exercise 1: Countdown to Liftoff")

print("Preparing for liftoff...")
for i in range(10,0,-1):
    print(i)

print("Liftoff! ")
print("--------------------------------\n")
# Exercise 2:
print("Exercise 2: Password Validation")
correct_password = "anhyeuem"

user_input = input("Enter the password: ")  
while user_input != correct_password:
    print("Incorrect password. Try again.")
    user_input = input("Enter the password: ")
print("Access granted!")
print("--------------------------------\n")
# Exercise 3:
print("Exercise 3: Find the first even number")
numbers = [1,3,9,15,8,11,12,7]

for num in numbers:
    if num % 2 == 0:
        print(f"The first even number is: {num}")
        break   