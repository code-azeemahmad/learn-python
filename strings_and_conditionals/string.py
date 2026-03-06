str1 = "code-"
str2 = 'azeem'
str3 = '''this is a string'''
str4 = "hello! this is joe's book"
str5 = "escape sequence characters.\nthis is next line"
print(str1 + str2)  # concatenation
print(len(str2))    # length

st = "code-azeem"
print(st[4])   # indexing
# strings are immutable. (you can't modify value stored at an index)

print(st[0 : 4])   # slicing
print(st[: 4])     # [0 : 4]
print(st[5 :])     # [0 : len(str)]

# backward counting starts from -1
print(st[-5 : ])
