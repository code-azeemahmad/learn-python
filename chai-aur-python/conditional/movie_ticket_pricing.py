# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# age = int(input("Enter your age: "))
# day = input("Enter the day: ")

# if age >= 18 and day == "wednesday":
#     print(12 - (12 * 0.02))
# elif age < 18 and day == "wednesday":
#     print(8 - (8 * 0.02))
# elif age >= 18:
#     print(12)
# else:
#     print(8)

age = 18
day = "tuesday"

price = 12 if age >= 18 else 8
if day == "wednesday":
    price -= 2
print("Your ticket  price is: $", price)

