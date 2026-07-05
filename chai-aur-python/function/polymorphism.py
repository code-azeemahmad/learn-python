# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def mul(a, b):
    return a * b

print(mul("O", 5))
print(mul(5, "X"))
print(mul(5, 5))

# 1. Polymorphism via "Duck Typing" in User Functions (Under the Hood: The Dunder Method Protocol)
# 2. Built-in Polymorphic Functions (The len() Example)
# 3. Class-Based Method Overriding (Inheritance Polymorphism)