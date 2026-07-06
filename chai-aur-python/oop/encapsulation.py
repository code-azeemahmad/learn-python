'''
Problem: Modify the Car class to encapsulate the brand attribute, 
making it private, and provide a getter method for it.
'''

class Car:

    def __init__(self, brand, model):
        self.__brand = brand    # private
        self.__model = model

    # @property makes a method behave like an attribute.
    @property
    def brand(self):    # not a pythonic way to name it getBrand
        return self.__brand
    
    @brand.setter
    def brand(self, newBrand):
        self.__brand = newBrand

    @property
    def model(self):
        return self.__model

myCar = Car("Tata", "Safari")
print(myCar.brand)
print(myCar.model)
myCar.brand = "Honda"
print(myCar.brand)

'''
leading underscore (_speed) means:
"This attribute is intended for internal use."

True Private Variables (__)
Python also supports name mangling using double underscores.
'''