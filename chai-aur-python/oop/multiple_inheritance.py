'''
Problem: Create two classes Battery and Engine, 
and let the ElectricCar class inherit from both, 
demonstrating multiple inheritance.
'''

# class Battery:
#     def __init__(self, type):
#         self.type = type

# class Engine:
#     def __init__(self, material):
#         self.material = material

# class ElectricClass(Battery, Engine):
#     def __init__(self, type, material):
#         Battery.__init__(self, type)
#         Engine.__init__(self, material)

# myEV = ElectricClass("Lithium-ion", "Aluminium")
# print(myEV.type)
# print(myEV.material)

# method resolution order mro

# Django version
class Battery:
    def __init__(self, type, **kwargs):
        super().__init__(**kwargs)
        self.type = type

class Engine:
    def __init__(self, material, **kwargs):
        super().__init__(**kwargs)
        self.material = material

class ElectricClass(Battery, Engine):
    def __init__(self, type, material):
        super().__init__(
            type = type,
            material = material
        )

myEV = ElectricClass("Lithium-ion", "Aluminium")
print(myEV.type)
print(myEV.material)
