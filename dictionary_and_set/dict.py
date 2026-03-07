# dictionaries are used to store data values in key:value pairs
# they are unordered, mutable and don't allow duplicate keys

info = {
    "key" : "value",
    "name" : "azeem",
    "age" : 21,
    "is_Student" : True,
    "marks" : 98.4,
    "topics" : ["learning, gaming, connecting"],
    "languages" : ("C++", "Java", "Python"),
    12 : "int key",
    6.4 : "float key",
    True : "bool key"
}

print(info)
print(type(info))

# all data types are acceptable as values
# lists and dictionaries cannot be used as keys because they are mutable

# Access value using key, not index
print(info["name"], info["age"])

# mutable
info["name"] = "shrewd"
print(info["name"])

# adding a new key value pair
info["surname"] = "warble"
print(info)

# adding a duplicate key overwrites the value


# empty dictionary
null_dict = {
    
}
print(null_dict)
null_dict["name"] = "code-azeem"
print(null_dict["name"])
