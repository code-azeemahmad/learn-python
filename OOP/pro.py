'''
Property Decorator:
    we use @property decorator on any method in the class to use the method as a property
'''

class Student:
    def __init__(self, phys, chem, math):
        self.phys = phys
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phys + self.chem + self.math) / 3) + "%"
        
        # def calcPer(self):
        #     self.percentage = str((self.phys + self.chem + self.math) / 3) + "%"
        
    @property
    def calcPercentage(self):
        return str((self.phys + self.chem + self.math) / 3) + "%"
        
stu1 = Student(23, 34, 45)
# print(stu1.percentage)
stu1.phys = 67
# print(stu1.phys)
# print(stu1.percentage)
# stu1.calcPer()
print(stu1.calcPercentage)      # call without (), It behaves like a variable but is actually a method.
        