
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