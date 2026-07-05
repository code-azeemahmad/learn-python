# Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10

while True:
    n = int(input("Enter some number: "))
    if 1 <= n <= 10:
        print("loop is terminated!")
        break
    else:
        print("bravo")


