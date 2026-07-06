'''
Problem: Demonstrate the use of isinstance to check 
 if my_tesla is an instance of Car and ElectricCar.
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

myEV = ElectricCar("Tesla", "Model S", "600 Watt")

print(isinstance(myEV, ElectricCar))
print(isinstance(myEV, Car))


