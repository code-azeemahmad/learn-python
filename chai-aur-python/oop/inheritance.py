'''
Problem: Create an ElectricCar class that inherits 
from the Car class and has an additional attribute
battery_size
'''
class Car:
    def __init__(self, brand, model):   # self points to current object
        self.brand = brand
        self.model = model
        
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)  # super() lets the child call methods from the parent class.
        self.batterySize = batterySize

myEV = ElectricCar("Tesla", "Model S", "600 Watt")
print(myEV.brand)
print(myEV.model)
print(myEV.batterySize)

