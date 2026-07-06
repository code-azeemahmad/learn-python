'''
Problem: Add a method to the Car class that displays the full name of the car (brand and model).
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def displayName(self):
        return f"Brand: {self.brand}, Model: {self.model}"
    
myCar = Car("Toyota", "Corolla")

print(myCar.displayName())