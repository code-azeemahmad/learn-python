collection = set()

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("code-azeem")
collection.add((1, 2, 3, 4))
# collection.add([1, 2, 3, 4])      # unhashable type: 'list'


collection.remove(4)        # removes the specific element

print(collection)

collection.clear()    # empties the set
print(len(collection))      # 0


collektion = {"hello", "world", "azeem", "code"}
print(collektion.pop())        # removes a random value

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))             # combines both set values and return new
print(set1.intersection(set2))      # combines common values and returns new