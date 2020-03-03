'''
Created on Mar 4, 2020

@author: bvikram2
'''
'''
Pandas
    It is a library for data manipulation and analysis.
    Series
    Dataframe
'''

import pandas as pd

cars = pd.Series(data=[10, 20, 30, "NA"], index=["bmw", "audi", "Lamb", "Hyundai"])

print(cars)
print(type(cars))
print(cars.shape)
print(cars.ndim)
print(cars.size)
print(cars.index)
print(cars.values)