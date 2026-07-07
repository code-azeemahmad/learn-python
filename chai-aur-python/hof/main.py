# Everything in Python is an object.

'''
A Higher-Order Function is simply a function that does at least one of these:
1) Takes another function a an argument.
2) Returns another function.
'''

def outer():

    def inner():
        print("Hello")

    return inner

# Both variables point to the same function.
x = outer()
x()