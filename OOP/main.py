# OOP in Python
# To map with real world scenarios, we started using objects in code
# This is called object oriented programming

class Student:
    name = "azeem"
    
s1 = Student()
print(s1.name)

class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

'''
All classes have a function called __init__(), 
which is always executed when the object is being initiated.
The self parameter is a reference to the current instance
of the class, and is used to access variables that belong
to the class
'''
class Student:
    # default constructor
    def __init__(self):
        pass
    
    # parametrized constructor
    def __init__(self, fullName, marks):
        print("adding new student to the database")
        self.name = fullName        # attributes
        self.marks = marks
    
s1 = Student("azeem", 98)
print(s1.name, s1.marks)
s2 = Student("bilal", 97)
print(s2.name, s2.marks)

