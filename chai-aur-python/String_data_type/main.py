# >>> username = "code-azeem"
# >>> print(username)
# code-azeem
# >>> firstChar = username[0]
# >>> print(firstChar)
# c
# >>> sliceName = username[:4]
# >>> print(sliceName)
# code
# >>> numList = "0123456789"
# >>> numList[:]
# '0123456789'
# >>> numList[3:]
# '3456789'
# >>> numList[:7]
# '0123456'
# >>> numList[0:7:2]
# '0246'
# >>> numList[0:7:3]
# '036'
# >>> username = "Code-Azeem"
# >>> print(username.lower())
# code-azeem
# >>> print(username.upper())
# CODE-AZEEM

# >>> username = "   azeem         "
# >>> print(username)
#    azeem         
# >>> print(username.strip())
# azeem
# >>> tea = "lemon tea"
# >>> print(tea.replace("lemon", "ginger"))
# ginger tea

# >>> tea = "Lemon, Ginger, Garlic, Honey"
# >>> print(tea.split(", "))    
# ['Lemon', 'Ginger', 'Garlic', 'Honey']

# >>> tea = "garlic tea"
# >>> print(tea.find("tea")) 
# 7
# >>> print(tea.find("y")) 
# -1
# >>> print(tea.count("tea"))
# 1

# >>> tea_type = "Lemon"
# >>> quantity = 2
# >>> order = "I ordered {} cups of {} tea"
# >>> order
# 'I ordered {} cups of {} tea'
# >>> print(order.format(quantity, tea_type))
# I ordered 2 cups of Lemon tea

# >>> tea_variety = ["lemon", "ginger", "garlic", "honey"]
# >>> tea_variety
# ['lemon', 'ginger', 'garlic', 'honey']
# >>> print("".join(tea)) 
# garlic tea
# >>> print("".join(tea_variety))
# lemongingergarlichoney
# >>> print(" ".join(tea_variety))
# lemon ginger garlic honey
# >>> print("-".join(tea_variety))
# lemon-ginger-garlic-honey
# >>> print(", ".join(tea_variety))
# lemon, ginger, garlic, honey

# >>> print(len(tea))
# 10
# >>> for letter in tea:
# ...     print(letter)
# ... 
# g
# a
# r
# l
# i
# c
 
# t
# e
# a

# >>> tea = "He said, \"lemon tea is awesome\"" 
# >>> print(tea)                               
# He said, "lemon tea is awesome"


# >>> tea = "lemon\ntea"
# >>> tea
# 'lemon\ntea'
# >>> print(tea)
# lemon
# tea
# >>> tea = r"lemon\ntea"
# >>> print(tea)         
# lemon\ntea
# >>> 

# >>> path = "C:\\user\\pwd" 
# >>> path
# 'C:\\user\\pwd'
# >>> print(path)
# C:\user\pwd

# >>> tea = "lemon tea"
# >>> print("lemon" in tea)
# True
# >>> print("lamon" in tea)
# False
