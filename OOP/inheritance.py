''''
Inheritance
when one class(child/ derived) derives the 
properties and methods of another class(parent/ base)
'''

class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started!")
    @staticmethod
    def stop():
        print("Car Stopped!")
    
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("sonata")

print(car1.start())
print(car2.color)

'''
i)   Single Inheritance (Parent --> Child)
ii)  Multilevel Inheritance (Parent --> Child --> Grandchild)
iii) Multiple Inheritance (Parent1, Parent2 --> Child)
'''

