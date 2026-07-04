# >>> tea_varieties = ["black", "pink", "green", "white"]
# >>> tea_varieties
# ['black', 'pink', 'green', 'white']
# >>> print(tea_varieties)
# ['black', 'pink', 'green', 'white']
# >>> print(tea_varieties[0])
# black
# >>> print(tea_varieties[1])
# pink
# >>> print(tea_varieties[-1])
# white

# >>> print(tea_varieties[1:3]) 
# ['pink', 'green']
# >>> print(tea_varieties[:2]) 
# ['black', 'pink']
# >>> print(tea_varieties[2:])
# ['green', 'white']

# >>> tea_varieties                
# ['black', 'a', 'l', 'm', 'o', 'n', 'd', 'green', 'herbal']
# >>> tea_varieties = ["black", "pink", "green", "white"]
# >>> tea_varieties[1:2] = ["almond"]
# >>> tea_varieties                  
# ['black', 'almond', 'green', 'white']
# >>> tea_varieties[1:3]
# ['almond', 'green']
# >>> tea_varieties[1:3] = ["hazelnut", "cashew"]
# >>> tea_varieties
# ['black', 'hazelnut', 'cashew', 'white']

# insert nothing (delete)
# >>> tea_varieties[1:2]                         
# ['test']
# >>> tea_varieties[1:3]
# ['test', 'test']
# >>> tea_varieties[1:3] = []
# >>> tea_varieties          
# ['black', 'hazelnut', 'cashew', 'white']


# >>> for tea in tea_varieties:
# ...     print(tea)
# ... 
# black
# hazelnut
# cashew
# white
# >>> for tea in tea_varieties:
# ...     print(tea, end="-")  
# ... 
# # black-hazelnut-cashew-white->>> 


# >>> tea_varieties            
# ['black', 'hazelnut', 'cashew', 'white']
# >>> if "oolong" in tea_varieties:     
# ...     print("oolong tea is present")
# ... 
# >>> tea_varieties.append("oolong")
# >>> if "oolong" in tea_varieties:     
# ...     print("oolong tea is present")
# ... 
# oolong tea is present
# >>> tea_varieties.pop()               
# 'oolong'
# >>> tea_varieties                     
# ['black', 'hazelnut', 'cashew', 'white']



