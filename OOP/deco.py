'''
Static Methods
Methods that don't use the self parameter (work at class level)

class Student:
    @staticmethod   # decorator
    def college():
        print("ABC")
        
* Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it    
'''

class Student:
    collegeName = "ABC College"
    def __init__(self, fullName, marks):
        self.name = fullName    
        self.marks = marks
        
    @staticmethod
    def hello():
        print("hello boya! ")
        
    def getMarks(self):
        print("Marks:", self.marks)    
        
        
s1 = Student("azeem", 98)
print(s1.name, s1.marks, s1.collegeName)
s2 = Student("bilal", 97)
print(s2.name, s2.marks, s2.collegeName)

# staticmethod means: The method does not depend on class or object data
Student.hello()
s1.hello()



