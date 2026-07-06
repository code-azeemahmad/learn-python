
# enumerate(iterable, start=0)

colors = ["Red", "Green", "Blue"]

for i in enumerate(colors, start=0):
    print(i)

for index, i in enumerate(colors, start=0):
    print(index, i)

'''
enumerate() is used when you need both the element 
and its position (index) while looping through a collection.
Example 1: Numbering Items
Example 2: Finding an Item's Position
Example 3: Detecting Even/Odd Positions
Example 4: Processing Data
'''