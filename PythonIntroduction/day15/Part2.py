'''
Created on Feb 14, 2020

@author: bvikram2
'''

'''
Multilevel Inheritance
'''


class A:

    def m1(self):
        print("A")


class B(A):

    def m2(self):
        print("B")

        
class C(B):

    def m3(self):
        print("C")        


ob = C()
ob.m1()
ob.m2()
ob.m3()
