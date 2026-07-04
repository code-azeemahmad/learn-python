# list - order matters
# dict - order does not matter

# >>> things = {"sky": "blue", "night": "black", "wall": "white"}
# >>> things
# {'sky': 'blue', 'night': 'black', 'wall': 'white'}
# >>> print(things["sky"])
# blue
# >>> things.get("night") 
# 'black'
# >>> things.get("nights")
# >>> print(things["ski"]) 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     print(things["ski"])
#           ~~~~~~^^^^^^^
# KeyError: 'ski'

# >>> things
# {'sky': 'blue', 'night': 'black', 'wall': 'white'}
# >>> things["night"] = "romantic" 
# >>> things
# {'sky': 'blue', 'night': 'romantic', 'wall': 'white'}