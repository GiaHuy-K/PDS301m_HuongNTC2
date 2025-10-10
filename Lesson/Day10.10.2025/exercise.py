class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
p1 = People("Alice", 30)
print(p1.display_info())

class Student(People):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Student ID: {self.student_id}"

s1 = Student("Bob", 20, "S123")
print(s1.display_info())
