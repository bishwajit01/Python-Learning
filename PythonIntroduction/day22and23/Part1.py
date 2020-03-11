'''
Created on Mar 4, 2020

@author: bvikram2
'''
'''
Pandas
    It is a library for data manipulation and analysis.
    Series : It is a 1-Dimensional data structure with labeled rows and column.
    DataFrame : It is a 2-Dimensional data structure with labeled rows and column.
'''

import pandas as pd

cars = pd.Series(data=[10, 20, 30, "NA"], index=["bmw", "audi", "Lamb", "Hyundai"])

print(cars)
print("===============")
print(type(cars))
print(cars.shape) # shape : Number of values.
print(cars.ndim) # dimensions in pandas.
print(cars.size) # Size of the Pandas.
print(cars.index) # index of the Pandas.
print(cars.values) # Values of a Pandas.