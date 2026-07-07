# map create a new list
# map(function, iterable)   # list comprehensions are preferred

def square(num):
    return num * num

num = [1, 2, 3, 4, 5]

# new_num = map(square, num)

new_num = map(lambda x:x * x, num)

# print(list(new_num))

numbers = ["10", "20", "30"]

int_list = map(int, numbers)
print(list(int_list))

# map does not return a list because map() is lazy

result = map(int, ["1", "2"])

print(list(result))
print(list(result)) # [] because iterators are consumed as you iterate over them

prices = ["100", "250", "300", "450"]
print(list(map(int, prices)))