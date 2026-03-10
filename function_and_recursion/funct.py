print("built-in", end=" and ")
print("user-defined function")

a = 5
b = 10
print(a + b)

# to avoid redundancy

def hello():
    print("print hello world")      # returns NULL

def sum(a, b):
    return a + b

print(sum(1, 2))
# print(hello())        # None
hello()

def pro1(a = 8, b =7):       # default parameters
    return a * b

print(pro1())

def pro2(a, b = 2):      #(non-default, default)
    return a * b

print(pro2(3))


def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
calc_fact(6)    