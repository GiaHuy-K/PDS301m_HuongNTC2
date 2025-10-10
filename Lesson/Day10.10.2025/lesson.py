class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def show(self):
        print("Name: ",self.name)
        print("Color: ",self.color)
    
#creating object of the class
obj =  Fruit("Apple","red")

#Modifying Object Properties
obj.name = "Strawberry"

#Calling the instance method using the object obj
obj.show()

#Output Fruit is strawberry and Color is red

class Employee:
    department = "IT"
    
    def show(self):
        print("Department: ",self.department)
        
emp = Employee()
emp.show()
#Delete object
del emp

#Accessing class after deleting object
emp.show()  # This will raise an error since emp is deleted
