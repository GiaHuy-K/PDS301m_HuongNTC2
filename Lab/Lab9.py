#Exercise 1:
class Student:
    """Represents a student with a name and ID, and enrolled courses."""
    def __init__(self, name,student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} has been enrolled in {course_name}.")
    
    def display_info(self):
        """Display student information."""
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled courses: {', '.join(self.courses) if self.courses else 'None'}")

#Create an object (instance) of the Student class
student1 = Student("Alice", "S12345")

#Use the object methods
student1.enroll("Python Programming")
student1.enroll("Data Structures")
student1.display_info()


print("--------------------------------\n")
# Exercise 2:
print("Exercise 2: Safe number input")
while True:
    try:
        age_str = input("Enter your age: ")
        age = int(age_str)
        print(f"You are {age} years old.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid age.")
print("--------------------------------\n")

# Exercise 3:
print("Exercise 3: Safe Division Function")

def divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    finally:
        print("Division attempt finished.")

#--- Test the function ---
print(f"Result: {divide(10,2)}") 
print("-"* 20)
print(f"Result: {divide(5,0)}") 
print("--------------------------------\n")