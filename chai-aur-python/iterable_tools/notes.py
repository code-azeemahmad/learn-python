'''
>>> ref = open('tool.py')
>>> ref.readline()
'import time\n'
>>> ref.readline()
'print("main is python file")\n'
>>> ref.readline()
'username = "Nadeem"\n'
>>> ref.readline()
'print(username)\n'
>>> ref.readline()
'\n'
>>> ref.readline()
''  # StopIteration exception
'''

# raw way (__next__() makes things iterable)
'''
>>> ref = open('tool.py')
>>> ref.__next__()
'import time\n'
>>> ref.__next__()
'print("main is python file")\n'
>>> ref.__next__()
'username = "Nadeem"\n'
>>> ref.__next__()
'print(username)'
>>> ref.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    ref.__next__()
    ~~~~~~~~~~~~^^
StopIteration
'''
# readline() bts handles the exception nicely

'''
>>> ref = open('tool.py')
>>> for line in ref:     
...     print(line, end='')
... 
import time
print("main is python file")
username = "Nadeem"
print(username)
>>> 
'''

'''
>>> while True:
...     line = ref.readline()
...     if not line: break
...     print(line, end='')
... 
import time
print("main is python file")
username = "Nadeem"
print(username)
>>> 
'''

'''
>>> test = "azeem"
>>> if not test:
...     print("empty")
... 
>>> test = "" 
>>> if not test:
...     print("empty")
... 
empty
'''

'''
>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x0000020A2ED905B0>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x0000020A2ED905B0>    # always point to starting address
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
'''

'''
>>> ref = open('tool.py')
>>> iter(ref) is ref    # file is itself iterable
True
'''

'''
>>> myList = [1, 2, 3] 
>>> iter(myList) is myList
False
'''

'''
>>> myDict = {"a": 1, "b": 2}
>>> for key in myDict.keys():
...     print(key)
... 
a
b
>>> I = iter(myDict)
>>> I
<dict_keyiterator object at 0x0000020A30D267F0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
'''

'''
>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> I          
<range_iterator object at 0x0000020A2EF78330>
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
'''