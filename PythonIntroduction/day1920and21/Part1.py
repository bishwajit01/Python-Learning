'''
Created on Feb 26, 2020

@author: Bishwajit.
'''
'''
NumPy
    Numeric Python
    It is open source library available in python.
    It is used in mathematical, engineering, scientific and data science programming.
    It deals with multi dimensional arrays.
'''

import numpy as np
import time

a = np.random.random(10000000)
print(type(a))
print(a)

# primitive way to get the Mean
startTime = time.time()
mean = sum(a) / len(a)
print("Time taken using old technique:: ", time.time() - startTime)

# using NumPy
startTime = time.time()
mean = np.mean(a)
print("Time taken by NumPy:: ", time.time() - startTime)
