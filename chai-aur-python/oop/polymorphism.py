'''
Polymorphism
Problem: Demonstrate polymorphism by defining a method 
fuel_type in both Car and ElectricCar classes, but
with different behaviors.
'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuelType(self):
        return "Petrol or Disel"
        
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuelType(self):
        return "Electric Charge"


myCar = Car("Honda", "Civic")
print(myCar.fuelType())

myEV = ElectricCar("Tesla", "Model S", "600 Watt")
print(myEV.fuelType())