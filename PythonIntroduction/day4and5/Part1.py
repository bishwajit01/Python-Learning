'''
Created on Jan 28, 2020

@author: bvikram2
'''

# Arrays is a collection of Homogeneous Elements.

'''
List Data Types.
    It is a collection of Heterogeneous Data Type.
    Elements are enclosed in []
    Elements are separated by comma.
    It is mutable.
    Elements will have its own unique Index number.
    Supports Forward and Backward Indexing.
    Insertion Order is preserved in list.
    Duplicated values are allowed.
'''
a = ["apples", 2, 75.89, True]
b = ["oranges", 4, 43.2, False]
c = [4, 7]
print(a)
print(type(a))

a.append(b)
print(a)
print(b[1])
print(b[-1])
print(b[1:])
print(b[1:3])
print(b[:3])
print(b[-1::])

# Concatenation.
print(b + c)

# Multiplication
print(c * 2)

# List packing
a = 4
b = "Hello"
c = 4 + 3j
list1 = [a, b, c]
print(list1)

# List Unpacking
x, y, z = list1
print(x)
print(y)
print(z)

# Nested List
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [a, b]
print(c)
print(c[1])
print(c[1][2])

# String to List
a = "My name is Bishwajit."
print(a.split())

# List to String
list1 = ["a", "b", "c"]
string1 = "".join(list1)
string2 = ".".join(list1)
print(string1)
print(string2)
