'''
Created on Apr 16, 2020

@author: Bishwajit.
'''

x = 50


def fun(x):
    print('x is', x)
    x = 2
    print('changed local x to', x)


fun(x)
print('x is now', x)