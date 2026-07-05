# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

import random
# act = random.choice(activity) # can't use random on dictionary

activity = {"sunny": "Go for a walk",
            "rainy": "Read a book",
            "snowy": "Build a snowman"}

keysList = list(activity.keys())   # convert dict to list of keys
key = random.choice(keysList)   #  store choice in key
print(key, ":", activity[key])  #  access key values

# In the software engineering world, 
# this design pattern is called a Lookup Table 
# or Dispatch Table. Instead of making 
# the CPU evaluate conditions line-by-line, 
# you map choices directly in memory. 
# It is highly readable and scalable.