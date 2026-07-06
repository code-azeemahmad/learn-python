'''
Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
'''

class Car:
    # contructor
    def __init__(self, brand, model):   # self is context just like this in js
        self.brand = brand  # attribute
        self.model = model
    
myCar = Car("Toyota", "Corolla")    # instance
print(myCar.brand)
print(myCar.model)

myNewCar = Car("Honda", "Civic")
print(myNewCar.brand)
print(myNewCar.model)