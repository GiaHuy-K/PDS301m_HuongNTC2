class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class University:
    def __init__(self, university_name, location):
        self.university_name = university_name
        self.location = location

    def display_university_info(self):
        return f"University: {self.university_name}, Location: {self.location}"
    
class Student(People, University):
    def __init__(self, name, age, student_id, university_name, location):
        People.__init__(self, name, age)
        University.__init__(self, university_name, location)
        self.student_id = student_id

    def display_info(self):
        base_info = People.display_info(self)
        university_info = University.display_university_info(self)
        return f"{base_info}, Student ID: {self.student_id}, {university_info}"
    
s1 = Student("Huy", 20, "S123", "XYZ University", "HCM City")
print(s1.display_info())
s2 = Student("Hao", 22, "S456", "ABC University", "Ha Noi ")
print(s2.display_info())