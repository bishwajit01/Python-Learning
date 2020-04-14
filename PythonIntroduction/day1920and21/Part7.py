'''
Created on Mar 2, 2020

@author: Bishwajit.
'''
'''
NumPy
'''

import numpy as np

# Single Dimension Array
a = np.arange(1, 17).reshape(4, 4)
print(a)
print(type(a))

# Slicing only 3X3
b = a[0:3, 0:3]
print(b)

# Slicing only 2X2
b = a[0:2, 0:2]
print(b)

# Slicing only 2X2
b = a[2:4, 2:4]
print(b)

# Slicing only 4X4
b = a[:4, :4]
print(b)

# Slicing only 2X2
b = a[2:, 2:]
print(b)
