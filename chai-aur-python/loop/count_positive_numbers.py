# count positive numbers in list
# Problem: Given a list of numbers, count how many are positive.

num = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10, -11]

count = 0
for i in num:
    # print(i)
    if (i < 0):
        count += 1

print(count)