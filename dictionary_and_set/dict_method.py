student = {
    "name" : "azeem",
    "subject" : {
        "chem" : 98,
        "phys" : 95,
        "math" : 93,
    }
}

print(student.keys())   # return all outer keys
print(student.values())   # return all values
print(len(student))     # total no of keys

print(student.items())  # return all (key, val) pairs as tuples


print(student.get("name"))      # returns None
print(student["name"])      # returns error


# newDict = {"city" : "atlanta"}
# student.update(newDict)

student.update({
    "city" : "atlanta"
})

print(student)

# type casting
# print(list(student.keys()))
# print(list(student.values()))