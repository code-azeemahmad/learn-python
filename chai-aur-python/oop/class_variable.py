'''
Problem: Add a class variable to Car that 
keeps track of the number of cars created.
'''

class Car:
    #  class variable
    count = 0   # There should be only one copy of it, shared by all objects.
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.count += 1  # Since count belongs to the class, update it through the class.

    @classmethod
    def carsCreated(cls):   # cls refers to the class, just like self refers to the instance.
        return cls.count
    
    '''cls.count is preferred over Car.count inside a class method because 
    it also works correctly if another class inherits from Car.'''
    
myCar1 = Car("Toyota", "Corolla")
myCar2 = Car("Toyota", "Corolla")
myCar3 = Car("Toyota", "Corolla")
myCar4 = Car("Toyata", "Corolla")

print(Car.carsCreated())