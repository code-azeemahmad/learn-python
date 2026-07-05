# List Uniqueness Checker
# Problem: Check if all elements ih a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = [1, 2, 3, 4, 5, 5, 4]

# for i in items:   # nested loop O(n^2)
#     count = 0
#     for j in items:
#         if i == j:
#             count += 1
#     if count > 1:
#         print(i)

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item:", item)
    unique_items.add(item)