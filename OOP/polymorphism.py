class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
        
    # def add(self, num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal, newImg)
    
    # we can define logic using dunder functions
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num2 = Complex(4, 6)
num1.showNumber()
num2.showNumber()

# num = num1.add(num2)
num = num1 + num2     # logic is not defined to use '+' operator for two objects of complex class
num = num2 - num1     # operator overloading (implementation of polymorphism) changed the meaning of sub function
num.showNumber()