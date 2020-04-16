'''
Created on Apr 16, 2020

@author: bvikram2
'''

a = [14, 52, 7]
b = a.copy()
print(b is a)

b = [2, 3, 4, 5]
a = list(filter(lambda x: x % 2, b))
print(a)
