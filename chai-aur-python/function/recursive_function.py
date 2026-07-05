'''
Problem: Create a recursive function to 
calculate the factorial of a number.
'''

def recFact(n):
    if n == 1:  # thinks about exit strategy
        return 1
    return n * recFact(n - 1)

print(recFact(6))

# RecursionError: maximum recursion depth exceeded