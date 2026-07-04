# Python Shell Commands

```python
# Addition
>>> 3 + 5
8

>>> 3 + 4
7

# Multiplication with variables
>>> score = 101
>>> score * 4
404

>>> print("hello world")
hello world

# String multiplication (repetition)
>>> "chai" * 3
'chaichaichai'

>>> # hello

# NameError - undefined variable
>>> tea
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea
NameError: name 'tea' is not defined

>>> impo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    impo
NameError: name 'impo' is not defined

>>> import os
>>> os.getcwd()
'F:\\python learning\\learn-python\\chai-aur-python\\basics'

>>> for c in "chai":
...     print(c)
... 
c
h
a
i

>>> import sys
>>> sys.platform
'win32'

# Module Imports and Reloading
# Initial import of custom module
>>> import hello_python 
Hello, Python!
lemon tea

# Calling module functions
>>> hello_python.chai("mint chai")
'mint chai'

# Accessing module attributes
>>> hello_python.chai1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    hello_python.chai1
AttributeError: module 'hello_python' has no attribute 'chai1'. Did you mean: 'chai'?

# Importing reload functionality
>>> from importlib import reload

# Reloading the module to get updated attributes
>>> reload(hello_python)
Hello, Python!
lemon tea
<module 'hello_python' from 'F:\\python learning\\learn-python\\chai-aur-python\\basics\\hello_python.py'>

# Accessing newly added module attributes after reload
>>> hello_python.chai1          
'masala tea'
>>> hello_python.chai3
'boba tea'
>>> hello_python.chai2
'pink tea'
