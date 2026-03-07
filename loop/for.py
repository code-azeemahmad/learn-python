# for sequential traversal

nums = [1, 2, 3, 4, 5, 6]
tup = (1, 2, 3, 4, 5, 6)

for val in tup:
    print(val)


str = "code-azeem"

for char in str:
    if (char == "o"):
        print("o found")
        break       # prevents else to execute
    print(char)
else:
    print("loop ended")     # exucute when the loop has completed
    
    
'''
Range()
    Range functions returns a seqence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
    range(start?, stop, step?)
'''

print(range(5))
seq = range(5)
# print(seq[1])
# print(seq[2])

for i in seq:
    print(i)

for i in range(10):
    print(i)
    
for k in range(0, 100, 2):
    print(k)
    
# start → included
# stop  → NOT included


"""
pass
    pass is a null statement that does nothing. It is used as a placeholder for future code
"""

for i in range(5):
    pass
if ( i < 5):
    pass
print("some usefull work")

# WAP to find the sum of first n natural numbers
n = 5
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

# WAP to find the factorial of first n numbers
n = 5
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print(fact)