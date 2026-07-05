# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def calCircle(r):
    area = r * r
    circumference = 3.1415 * area
    return (area, circumference)    # pack in a tuple

(area, circumference) = calCircle(2)    # tuple unpacking
print("Area:", area, "and", "Circumference:", circumference)

def circle(r):
    a = r*r
    c = math.pi * a
    return a, c
a, c = circle(2)    # Option A: Multiple Variable Unpacking
print(a, math.ceil(c))


def circle(r):
    a = r*r
    c = math.pi * a
    return a, c
oneImmutableTuple = circle(2)   # Option B: Capture as a Single Group
print(oneImmutableTuple[0])
print(math.ceil(oneImmutableTuple[1]))