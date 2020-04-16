'''
Created on Apr 16, 2020

@author: Bishwajit.
'''

a, b = 6, 7
a, b = b, a
print(a, b)

a = (1)
print(type(a))

b = (1,)
print(type(b))

tup = (1, 2, 3, 4)
tup.append((5, 6, 7))
#print(len(tup)) # error tuple' object has no attribute 'append'
