'''
Created on Apr 20, 2020

@author: Bishwajit.
'''


def fun(n):
    if (n > 100):
        print(n, " ", end = " ")
        return n - 5
    print(n, " ", end = " ")
    return fun(fun(n + 11));


a = fun(45)
print(a)