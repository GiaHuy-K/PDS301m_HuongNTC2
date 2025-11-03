#Exercise 1
print("Exercise 1: Age Verification")
age_str = input("Enter your age: ")
age = int(age_str)
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
print("--------------------------------\n")

#Exercise 2
print("Exercise 2: Number Classification")
number_str = input("Enter a number: ")
number = int(number_str)

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
print("--------------------------------\n")
#Exercise 3
print("Exercise 3: Roller Coaster Access")
height_str = input("Enter your height in cm: ")
height = float(height_str)

age_str = input("Enter your age: ")
age = int(age_str)

if height >= 140 and age >= 12:
    print("Access granted!")
else:
    print("Access denied!")