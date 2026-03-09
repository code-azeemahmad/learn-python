'''
class method
A class method is bound to the class and receives the class as an implicit first argument.
Note - static method can't access or modify class state and generally for utility
'''
class Person:
    name = "anonymous"
    # def changeName(self, name):
        # self.name = name
        # Person.name = name
        # self.__class__.name = "Joe"
        
        # if we want to directly access our class inside the function --> class methods
        
    @classmethod        # decorators
    def changeName(cls, name):
        cls.name = name
            
p1 = Person()
p1.changeName("Joe")
print(p1.name)
print(Person.name)      # we have to change class attribute\
    
    
'''
1) static methods
2) class methods(cls)
3) instance methods(self)
'''
