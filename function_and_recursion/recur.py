def show(n):
    if (n == 0):        # base case
        return
    print(n)
    show(n - 1)
    print("end")
    
show(3)


# call stack
# |         |
# |-show(0)-|   stacks deleted and return
# |-show(1)-|
# |-show(2)-|
# |-show(3)-|
# |_________|

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * fact(n - 1)     

print(fact(5))