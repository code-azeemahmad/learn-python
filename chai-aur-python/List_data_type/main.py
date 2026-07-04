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

# >>> tea_varieties.remove("hazelnut")
# >>> tea_varieties
# ['black', 'cashew', 'white']
# >>> tea_varieties.insert(1, "green")
# >>> tea_varieties
# ['black', 'green', 'cashew', 'white']


# >>> tea_varieties  
# ['black', 'green', 'cashew', 'white']
# >>> tea_varieties_copy = tea_varieties    // both share same reference
# >>> tea_varieties_copy = tea_varieties.copy() // breaks the link, creates a new list
# >>> tea_varieties_copy                       
# ['black', 'green', 'cashew', 'white']
# >>> tea_varieties_copy.append("imposter")
# >>> tea_varieties
# ['black', 'green', 'cashew', 'white']
# >>> tea_varieties_copy
# ['black', 'green', 'cashew', 'white', 'imposter']

# >>> squared_nums = [1, 2, 3, 4, 5, 6,  7,  8, 9, 10]
# >>> range(10)
# range(0, 10)
# >>> y = range(0, 10)
# >>> print(y)
# range(0, 10)
# >>> squared_nums = [x** 2 for x in range(0, 10)]    
# >>> squared_nums                                
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> cube_num = [y**3 for y in range(0, 5)]
# >>> cube_num
# [0, 1, 8, 27, 64]
