'''
Created on Mar 2, 2020

@author: Bishwajit.
'''
'''
NumPy
    Numpy Array is mutable.
'''

import numpy as np

# Single Dimension Array
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(type(a))

# Negative Indexing
print(a[-1])
# Positive Indexing
print(a[4])

a[1] = 40
print(a[1])

# Double Dimension Array Indexing
a = np.arange(1, 10).reshape(3, 3)
print(a)
print(a[1, 2])

# Three Dimension Array Indexing
a = np.arange(1, 9).reshape(2, 2, 2)
print(a)
print(a[1, 1, 1])
print(a[0, 1, 1])
print(a[1, 0, 1])
print(a[1, 1, 0])
