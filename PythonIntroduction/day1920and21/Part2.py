'''
Created on Feb 26, 2020

@author: bvikram2
'''
'''
Arrays Using Traditional Way
'''

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a)
print(type(a))
print(a.size)
# shape = total number of elements
print(a.shape)

print("***********************")
a = np.array([1, 2, 3, 4, 5, 6, 7, [1, 2, 3, 4, 5, 6, 7]])
print(a)
print(type(a))
print(a.shape)
print(a.size)

print("***********************")
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(type(a))
print(a.shape)
print(a.size)

print("***********************")
a = np.array([["Bishwajit", "Vikram"], ["python", "java"]])
print(type(a))
print(a.shape)
print(a.size)
