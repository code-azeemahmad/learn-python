class Student:
    # class attribute
    collegeName = "ABC College"     # common to all objects (stored in memory only once)
    def __init__(self, fullName, marks):
        self.name = fullName    # object attribute
        self.marks = marks
        
    def welcome(self):
        print("welcome student!", self.name)
        
    def getMarks(self):
        print("Marks:", self.marks)    
        
        
s1 = Student("azeem", 98)
print(s1.name, s1.marks, s1.collegeName)
s2 = Student("bilal", 97)
print(s2.name, s2.marks, s2.collegeName)
s1.welcome()
s1.getMarks()

print(Student.collegeName)