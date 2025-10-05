#Exercise 1: 
print("Exercise 1: Simple Area Calculator")
def calculate_area(width,height):
    """Calculate the area of a rectangle"""
    return width * height

area = calculate_area(5,10)
print(f"The area of the rectangle is: {area}")
print("--------------------------------\n")

#Exercise 2:
print("Exercise 2: Checking for the even number")
def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")
print("--------------------------------\n")
#Exercise 3:
print("Exercise 3: Temperature Converter")
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")
print("--------------------------------\n")