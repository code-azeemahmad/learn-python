# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    # print(*args)
    # print(args) # tuple
    # for i in args:
    #     print(i * 2)

    return sum(args)

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5, 6))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
'''
the variable args behaves purely as a standard 
tuple containing all the loose inputs passed 
to the function call site. packing and unpacking.
'''