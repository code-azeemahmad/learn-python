'''Problem: Use a property decorator in the Car 
class to make the model attribute read-only.'''

class Car:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model

myCar = Car("Toyata", "Corolla")

print(myCar.model)
# myCar.model = "Civic"   # property 'model' of 'Car' object has no setter
# It is Read-Only
# Because you only defined a getter and not a setter, Python won't allow assignments

