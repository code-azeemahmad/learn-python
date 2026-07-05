# Problem: Create a lambda function to compute the cube of a number.

# lambda  arguments : expression
cube = lambda a: a**3   # django/ flask
print(cube(2))
print((lambda b: b ** 3)(3))    # IIFE

anotherCube = cube  # exact same memory address allocation
print(anotherCube(3))

# under the hood
'''
Anonymity: 
A lambda function's __name__ property is 
automatically bound to the generic string "<lambda>", 
whereas a def function stores its actual structural name.

Expression Limit: 
Lambda functions are strictly 
restricted by the Python parser to contain exactly 
one single expression. You cannot write multi-line 
loops, docstrings, or complex variable assignments 
inside a lambda body.
'''