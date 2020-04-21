'''
Created on Apr 21, 2020

@author: Bishwajit.
'''

x = 12


def f1(a, b=x):
    print(a, b)

    
x = 15
f1(4)


def f2():
    x = 15
    print(x)


x = 12
f2()
