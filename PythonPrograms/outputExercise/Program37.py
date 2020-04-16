'''
Created on Apr 16, 2020

@author: Bishwajit.
'''

s = set()
print(type(s))

a = frozenset(set([5, 6, 7]))
print(a)

a = {5, 6, 7, 8}
b = {7, 5, 6, 8}
print(a == b)

a = {5, 4}
b = {1, 2, 4, 5}
print(a < b)

a = {4, 5, 6}
b = {2, 8, 6}
# print(a + b) # error supported operand types.
