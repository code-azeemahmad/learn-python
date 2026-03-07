# Tuples is A built-in data type to create immutable sequences of values.
# Tuples are immutable just like strings

num = (1, 2, 3, 4, 5, 6, 7, 8,)     # ending , is optional for multiple values in a tuple
print(type(num))
print(num[0])
# num[0] = 10     'tuple' object does not support item assignment
print(num)

tup = ()
print(type(tup))
tup = (1)
print(type(tup))    # int
tup = ("azeem")
print(type(tup))    # string

tup = (1,)      # , is mandatory for a single value to be percieved as a tuple
print(type(tup))
