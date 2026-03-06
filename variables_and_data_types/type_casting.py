# type convertion (automatically)

a = 3
b = 2.5      # superior (extra info)
sum = a + b
print(sum)
print(type(sum))

# type casting (manually)

s = "5"
sum = a + b + int(s)
print(sum)
print(type(sum))

pi = 3.14
pi = str(pi)
print(pi)
print(type(pi))