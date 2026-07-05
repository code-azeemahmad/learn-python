'''
Problem: Write a generator function that yields 
even numbers up to a specified limit.
'''

# standard function implementation (Eager Evaluation)
'''
def even_generator(n):
    l = []
    for i in range(1, n+1, 2):
        if (i % 2 == 0):
            l.append(i)
    return l

print(even_generator(10))   # it returns a list, but we want actual 2, 4, 6, 8, 10
'''

# generator function (Lazy Evaluation)
def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield(i)    # not return, generate on demand

# yield store that function and state of function in memory
gen = even_generator(10)    # returns a generator object
for num in gen:
    print(num, end=" ")


# Implementing lazy evaluation dramatically reduces memory consumption and prevents unneeded CPU overhead

'''
Your Original Code (Eager Evaluation)
Your code uses a standard list accumulation loop. 
If you call even_generator(1000000), Python must 
compute all one million numbers simultaneously, 
allocate a massive block of RAM to hold that list, 
and return the entire package at once. If your 
number is large enough, your program will crash 
with an OutOfMemoryError.

The True Generator (Lazy Evaluation)
When you use yield, Python completely alters the 
function's lifecycle. A generator does not compute
 everything upfront. Instead, it computes one single
   value at a time, on-demand, pausing its state 
   until you ask for the next one.

1) The Pause Control: When the loop hits yield i, 
the function doesn't terminate like a return 
statement would. Instead, it freezes its entire 
execution frame state (local variables, loop pointers) 
and hands the single value to the caller.

2) The Resume Trigger: The next time your program asks 
for a value (like in a for loop), the execution engine 
jumps directly back inside the generator right where 
it left off, increments the loop, and runs until it
hits the next yield.
'''




