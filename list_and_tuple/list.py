# List is A built-in data type that stores a set of values

marks1 = 34
marks2 = 56
marks3 = 89

marks = [34, 56, 89, 39, 67, 49, 100, 29]

print(marks)
print(marks[0])
print(type(marks))
print(len(marks))

# It can store elements of different types (integar, float, string)

student = ["azeem", 100, 21, "fountaine"]
print(student)

# Lists are mutable in python

student[0] = "bilal"
print(student)

# List Slicing (-ive indices start from -1)

print(marks[1 : 4])
