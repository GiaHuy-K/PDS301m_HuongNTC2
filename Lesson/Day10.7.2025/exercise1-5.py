# Bai tap 1. 
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
print("Exercise 1: ")
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)


# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()
print("\n--------------------------------")
vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
print("\n--------------------------------")
    

# Bai tap 2.
# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
print("Exercise 2: ")
class Bus(Vehicle):
    pass

bus1 = Bus(120, 18)
bus1.assign_seating_capacity(50)
bus1.display_properties()

# Bai tap 3.
# Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.
print("\n--------------------------------")
print("Exercise 3")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Area: {:.2f}".format(c.area()))
print("Perimeter: {:.2f}".format(c.perimeter()))

# Bai tap 4. 
# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
print("\n--------------------------------")
print("Exercise 4")

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  
    def calculate_age(self, current_year):
        birth_year = int(self.dob.split('-')[0])
        return current_year - birth_year

p1 = Person("Den Vau", "VietNam", "1989-05-13")
print(f"Name: {p1.name}, Country: {p1.country}, Date of Birth: {p1.dob}")
print(f"Age: {p1.calculate_age(2025)} years")
print("\n--------------------------------")

# Bai tap 5. 
# Write a Python program to create a  calculator class.
# Include methods for basic arithmetic operations.( +, -, *, /)

print("Exercise 5")
class Calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

calc = Calculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.subtract(a, b))
print("Multiplication:", calc.multiply(a, b))
print("Division:", calc.divide(a, b))