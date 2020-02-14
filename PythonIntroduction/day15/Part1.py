'''
Created on Feb 14, 2020

@author: bvikram2
'''
'''
Inheritance
    Single Inheritance
    Multiple Inheritance
    Multilevel Inheritance
    Hierarchical Inheritance
'''


# Single Inheritance
class A:

    def m1(self):
        print("Class A")


class B(A):
    pass  # empty class


a = B()
a.m1()
