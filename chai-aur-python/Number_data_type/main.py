# >>> x = 2
# >>> y = 3
# >>> z = 3
# >>> (x + y) * z
# 15
# >>> 40 + 2.34
# 42.34

# >>> 'azeem' + 3
# Traceback (most recent call last):
#   File "<python-input-8>", line 1, in <module>
#     'azeem' + 3
#     ~~~~~~~~^~~
# TypeError: can only concatenate str (not "int") to str

# # your intention should always be clear, (operation on same data types)
# >>> float(40)
# 40.0

# >>> 'code' + '-' + 'azeem'  # operator overloading
# 'code-azeem'

# + automatically detects operands on its left and right sides

# >>> x, y, z
# (2, 3, 3)
# >>> x + 1, y * 2
# (3, 6)
# >>> y % 2
# 1
# >>> z ** 2
# 9
# >>> 100 ** 2
# 10000
# >>> 2 ** 100
# 1267650600228229401496703205376
# >>> 2 * 1000
# 2000
# >>> 2 ** 1000
# 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

# >>> repr('chai')
# "'chai'"
# >>> str('chai')
# 'chai'
# >>> print('chai')
# chai

# >>> result = 1/3.0
# >>> result
# 0.3333333333333333



# >>> x = 2
# >>> y = 3
# >>> z = 4
# >>> x, y, z
# (2, 3, 4)
# >>> x < y < z
# True
# >>> x < y and y < z
# True
# >>> 1 == 2 < 3    # is automatically interpreted as: (1 == 2) and (2 < 3) 
# False
# >>> 1 == 2 and 2 < 3
# False

# >>> import math
# >>> math.floor(3.5)
# 3
# >>> math.floor(-3.5)
# -4
# >>> math.floor(3.6)
# 3
# >>> math.floor(3.9)
# 3
# >>> math.trunc(2.8)
# 2
# >>> math.trunc(-2.8)
# -2
# >>> 99999999999999999999999999999999 + 1
# 100000000000000000000000000000000
# >>> 99999999999999999999999999999999 * 2.1
# 2.1e+32
# >>> 2 ** 400
# 2582249878086908589655919172003011874329705792829223512830659356540647622016841194629645353280137831435903171972747493376


# >>> 2 + 3j
# (2+3j)
# >>> (2 + 3j) * 3
# (6+9j)

# >>> 0o20
# 16
# >>> 0xFF
# 255
# >>> 0b1000
# 8
# >>> oct(64)
# '0o100'
# >>> hex(64)
# '0x40'
# >>> bin(64)
# '0b1000000'

# >>> int(3.14)
# 3
# >>> int(32)
# 32
# >>> int('32', 8)
# 26
# >>> int('32', 16)
# 50
# >>> int('2', 16)
# 2
# >>> int('10000', 2)
# 16

# >>> x = 1
# >>> x << 2
# 4

# >>> import random
# >>> random.random()
# 0.20173593527987554
# >>> random.randint(1, 10)
# 5

# >>> l1 = ['lemon', 'onion', 'ginger', 'tomato', 'coriander']
# >>> random.choice(l1)
# 'tomato'
# >>> random.choice(l1)
# 'lemon'
# >>> random.choice(l1)
# 'ginger'


# >>> random.shuffle(l1)
# >>> l1
# ['onion', 'lemon', 'ginger', 'coriander', 'tomato']
# >>> random.shuffle(l1)
# >>> l1
# ['coriander', 'lemon', 'ginger', 'tomato', 'onion']

# >>> 0.1 + 0.1 + 0.4
# 0.6000000000000001
# >>> 0.1 + 0.1 + 0.1
# 0.30000000000000004
# >>> 0.1 +  0.1 + 0.1 - 0.3
# 5.551115123125783e-17
# >>> (0.1 +  0.1 + 0.1) - 0.3
# 5.551115123125783e-17
# >>> from decimal import Decimal
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')


# >>> from fractions import Fraction
# >>> myFra = Fraction(2, 7)
# >>> myFra
# Fraction(2, 7)


# >>> set1 = {1, 2, 3, 4}
# >>> set1 & {1, 3}
# {1, 3}
# >>> set1 | {1, 3, 5}
# {1, 2, 3, 4, 5}
# >>> set1 - {1, 2, 3, 4}
# set() # represent empty set with set()
# >>> type({})  # empty parenthesis represents empty dictionary
# <class 'dict'>


# >>> type(True)
# <class 'bool'>
# >>> True == 1
# True
# >>> True is 1
# <python-input-108>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> True
# True
# >>> True + 4
# 5
