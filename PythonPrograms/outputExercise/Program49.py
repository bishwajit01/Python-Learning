'''
Created on Apr 21, 2020

@author: Bishwajit.
'''

x = 100


def f1():
    global x
    x = 90


def f2():
    global x
    x = 80


print(x)
