# Sum of Even Numbers
# Problem: Cafculate the sum of even numbers up to a given number n.

n = 15
i = 0
sum = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

# Python deliberately chose not to include the increment (++) and decrement (--) operators in its language design.