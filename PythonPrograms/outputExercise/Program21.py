'''
Created on Apr 6, 2020

@author: Bishwajit.
'''

'''
Output Exercise
'''


def f(x):
    print("outer")

    def f1(a):
        print("inner")
        print(a, x)


f(3)
f1(1)
