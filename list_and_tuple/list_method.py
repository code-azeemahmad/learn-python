num = [2, 6, 3, 8, 1]
num.append(7)
print(num)

num.sort()
# print(num.sort())   # returns none
print(num)

num.sort(reverse = True)
print(num)

num.reverse()
print(num)

num.insert(3, 4)
num.insert(4, 5)
print(num)

num.remove(4)
print(num)

num.pop(3)
print(num)