'''
Created on Apr 20, 2020

@author: Bishwajit.
'''

l = [1, 2, 3, 4, 5]
m = map(lambda x: 2 ** x , l)
print(list(m))

l1 = [10, 20, 30]
l2 = l1
print(id(l1) == id(l2))

l2 = l1.copy()
print(id(l1) == id(l2))
