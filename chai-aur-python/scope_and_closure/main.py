
username = "code-azeem"

def func():
    username = "ahmad"
    print(username)

# print(username)
# func()

# x = 99

def func2(y):
    return x + y
# print(func2(1))

x = 99

def func3():
    global x    # Modifies the actual global variable directly
    x = 12      # avoid it, access it but not overwrite it
    return x

# print(func3())  # 12
# print(x)    # 12

def f1():
    x = 88
    def f2():   # closure (f2 takes x = 88 from f1)
        print(x)
    # f2()
    return f2   # reference
result = f1()
result()    # execute


def outer(num):
    def inner(x):
        return x ** num
    return inner

f = outer(2)    # reference of inner()
g = outer(3)

# def outer(2):
#     def inner(x):
#         return x ** 2
#     return inner

print(f(3)) # calc square
print(g(3)) # calc cube