'''
Created on Mar 2, 2020

@author: Bishwajit.
'''
'''
NumPy
'''
import numpy as np

# Single Dimension Array
a = np.array([2, 6, 2, 5, 8, 2, 7])
print(a)
print(type(a))

# appending in the single dimension array
a = np.append(a, [6, 9, 2, 5, 8])
print(a)

# double dimension array
a = np.arange(1, 10).reshape(3, 3)
print(a)
print(type(a))

# appending in the double dimension array
b = np.append(a, [[3, 7, 4]], axis=0)  # if axis =0, it is for the row. 
print(b)

b = np.append(a, [[4], [2], [7]], axis=1)  # if axis =0, it is for the row. 
print(b)
