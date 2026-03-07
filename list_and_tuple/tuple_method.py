tup = (1, 2, 3, 4, 1)
print(tup[0 : 2])

print(tup.index(3))     # return index of first occurence
print(tup.count(1))     # counts total occurences

# WAP to check if a list contains a palindrome or not

pal = [1, 2, 1]
pal_copy = pal.copy()
pal_copy.reverse()
if (pal_copy == pal):       # if (pal_copy.reverse() == pal): --> none == pal --> NOT
    print("IS a Palindrome")
else:
    print("Not a Palindrome")
    
    
