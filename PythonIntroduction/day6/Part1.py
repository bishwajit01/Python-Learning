'''
Created on Jan 28, 2020

@author: bvikram2
'''

'''
Tuples
    Same as List
    It is immutable.
    It is enclosed by ()
    It is separated by Comma(,)
    It can store heterogeneous elements.
    Insert and Append function won't work with Tuple because we cannot modify the tuples.
'''

a = (1, True, 4.8, "Hello")
print(a)
print(type(a))

b = 21, True, 4.8, "Hello"  # By default it acts as Tuple
print(type(b))

# Indexing
print(a[0])
print(b[1])
print(b[2])
print(b[-1])

# Slicing
print(b[1:])
print(b[::-1])
print(b[1:3])

# Concatenation
c = a + b
print(c)

# Multiplication
print(a * 2)
print(a[3] * 2)
