'''
Problem: Create a function that accepts any number of 
keyword arguments and prints them in the format key: value.
'''

# def print_kwargs(name, power):
#     print("Name:", name, "Power:", power)

# print_kwargs(name="Alice", power="Teleport")
# print_kwargs(power="Teleport", name="Alice")

def print_kwargs(**kwargs): # kwargs acts as an automated packing net that catches named variable assignments and packages them into a standard Python dictionary.
    for key, value in kwargs.items():   # breaks the dictionary down into pairs of items (key, value)
        print(f"{key}: {value}")

print_kwargs(name="Alice")
print_kwargs(name="Alice", power="Teleport")
print_kwargs(name="Alice", power="Teleport", enemy="Ghoul")

