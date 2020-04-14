'''
Created on Apr 6, 2020

@author: Bishwajit.
'''
'''
Output Exercise
'''


def foo(a, b=[]):
    b.append(a)
    return b


print(foo(2, [3, 4]))
