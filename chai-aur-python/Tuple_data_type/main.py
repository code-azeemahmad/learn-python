# >>> teaTypes = ("black", "green", "pink")
# >>> teaTypes
# ('black', 'green', 'pink')

# >>> print(type(teaTypes))  
# <class 'tuple'>

# >>> teaTypes[0]
# 'black'
# >>> teaTypes[-1]
# 'pink'
# >>> teaTypes[1:3]
# ('green', 'pink')
# >>> teaTypes[0] = "lemon"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     teaTypes[0] = "lemon"
#     ~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment