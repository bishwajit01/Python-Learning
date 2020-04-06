'''
Created on Apr 6, 2020

@author: bvikram2
'''
'''
Output Exercise
'''


def foo(a, b=[]):
    b.append(a)
    return b


print(foo(2, [3, 4]))
