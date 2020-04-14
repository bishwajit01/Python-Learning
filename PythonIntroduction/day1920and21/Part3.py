'''
Created on Feb 26, 2020

@author: Bishwajit.
'''
'''
Arrays Using Numpy
'''
import numpy as np

a = np.zeros((3, 4))
print(a)

print("***********************")
a = np.ones((2, 5))
print(a)

print("***********************")
a = np.full((3, 5), 9)
print(a)

print("***********************")
a = np.eye(3)
print(a)

print("***********************")
a = np.diag([10, 20, 30, 40])
print(a)

print("***********************")
a = np.arange(10)
print(a)

print("***********************")
a = np.arange(2, 10)
print(a)

print("***********************")
a = np.reshape(a, (4, 2))
print(a)
