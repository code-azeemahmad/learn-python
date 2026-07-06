'''Problem: Add a static method to the Car class 
that returns a general description of a car.'''

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    '''A static method is a method that belongs to the class, 
    but does not need access to the object (self) or the class (cls).'''

    @staticmethod   # independent of objects (can be called through object but should not be)
    def generalDesc():
        return "Cars are means of transport"
        
myCar = Car("Toyata", "Corolla")
print(Car.generalDesc())

