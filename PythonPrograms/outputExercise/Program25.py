'''
Created on Apr 15, 2020

@author: Bishwajit.
'''

a = 10
b = 20


def change():
    global b
    a = 35
    b = 56


change()
print(a)
print(b)
