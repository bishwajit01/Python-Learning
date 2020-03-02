'''
Created on Mar 2, 2020

@author: bvikram2
'''
'''
NumPy
'''
import numpy as np

# Single Dimension Array
a = np.array([2, 6, 2, 5, 8, 2, 7])
print(a)
print(type(a))

# inserting into Single Dimension Array
a = np.insert(a, 4, [6, 8, 2])
print(a)

# double dimension array
b = np.arange(1, 10).reshape(3, 3)
print(a)
print(type(a))

# inserting into Double Dimension Array
a = np.insert(b, 2, [3, 7, 1], axis=0)
print(a)

a = np.insert(b, 2, [3, 7, 1], axis=1)
print(a)
