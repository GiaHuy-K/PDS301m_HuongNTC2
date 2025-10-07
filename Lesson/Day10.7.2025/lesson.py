class Student:
    #class variable
    school_name = "FPT University"
    
    #constructor
    def __init__(self, name, age):
        #instance variables
        self.name = name
        self.age = age
    
    #instance method
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {self.school_name}")
        
    def change_age(self, new_age):
        #modify instance variable
        self.age = new_age
        
    #class method
    @classmethod
    def modify_school_name(cls, new_name):
        cls.school_name = new_name
    
s1 = Student("Huy", 20)
s1.show()
s1.change_age(21)
s1.show()
Student.modify_school_name("ABC University")
s2 = Student("Lan", 22)
s2.show()