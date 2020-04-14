'''
Created on Mar 12, 2020

@author: Bishwajit.
'''
'''
PANDAS
    DataFrame : It is a 2-Dimensional data structure with labeled rows and column. 
'''

import pandas as pd

carsData = {'showroom1': pd.Series(data=[10, 20, 30], index=['bmw', 'swift', 'Maruti']),
            'showroom2': pd.Series(data=[1, 2, 3], index=['bmw', 'swift', 'Maruti'])}

print(carsData)
print(type(carsData)) 

carsshowroom = pd.DataFrame(carsData)
print(carsshowroom)
print(type(carsshowroom))

carsData = {'showroom1': pd.Series(data=[10, 20, 30]), 'showroom2': pd.Series(data=[1, 2, 3])}
print(carsData)
print(type(carsshowroom))