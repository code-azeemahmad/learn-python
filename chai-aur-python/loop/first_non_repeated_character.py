# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

word = "teeter"
for i in word:
    count = 0
    for j in word:
        if i == j:
            count += 1
    if count == 1:
        print("First non-repeated character is:", i)
        break


# input_str = "teeter"

# for char in input_str:
#     if input_str.count(char) == 1:
#         print("Char is: ", char)
#         break