# check if a number is prime

n = 151
check = True
for i in range(2, n):
    if n % i == 0:
        check = False
        break

if check:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")


# develop the mental models behind everything

