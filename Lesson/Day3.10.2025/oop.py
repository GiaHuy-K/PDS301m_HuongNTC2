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

vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()


class Student:
    # class variable
    school_name = "FPT University"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Huy","21")
# access instance variables
print("Student: ",s1.name,s1.age)

# access class variables
print("School name: ", Student.school_name)

# modify instance variables
s1.name = "Huyk2"
s1.age = "32"
print("Student: ",s1.name,s1.age)

# modify class variables
Student.school_name = " Dai Hoc Thanh Hoa"
print("School name: ", Student.school_name)

# TODO: học lại OOP