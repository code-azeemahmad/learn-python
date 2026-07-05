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

# >>> things
# {'sky': 'blue', 'night': 'romantic', 'wall': 'white'}
# >>> for t in things:
# ...     print(t)
# ...
# sky
# night
# wall
# >>> for t in things:
# ...     print(t, things[t])
# ...
# sky blue
# night romantic
# wall white

# >>> for key, value in things.items():
# ...     print(key,":",value)         
# ... 
# sky : blue
# night : romantic
# wall : white

# >>> if "sky" in things:
# ...     print("The sky is blue!")
# ...
# The sky is blue!
# >>> print(len(things))
# 3