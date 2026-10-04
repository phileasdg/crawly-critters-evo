## COMING FROM WL ##

# There are many functions I miss from WL in python, so I've defined a few substitutes below.

## Dependencies

from collections.abc import Iterable

## Debugging:

def echo(x):
    print(x)
    return x

## List manipulation:

def first(list):
    return list[0]

def rest(list):
    return list[1:]

def most(list):
    return list[:-1]

def last(list):
    return list[-1]

def riffle(a, b):
    # Create a list of None elements of the combined length of a and b:
    out = [None] * (len(a) + len(b))
    # Assign all elements of a to the even positions:
    out[::2] = a
    # Assign all element of b to the odd positions:
    out[1::2] = b
    return out
