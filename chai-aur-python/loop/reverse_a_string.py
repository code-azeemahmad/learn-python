# Reverse a String
# Problem: Reverse a string using a loop.

phrase = "hello"
reversed_phrase = ""

# reversed_phrase = phrase[::-1]

i = len(phrase) - 1
while (i >= 0):
    reversed_phrase += phrase[i]
    i -= 1

print(reversed_phrase)


# phrase = "Python"
# chars_list = []  # A mutable array buffer
# i = len(phrase) - 1

# while i >= 0:
#     chars_list.append(phrase[i])  # O(1) in-place array update
#     i -= 1

# # Convert the final array back to a string all at once
# reversed_phrase = "".join(chars_list)  # Single O(n) string allocation allocation
# print(reversed_phrase)
