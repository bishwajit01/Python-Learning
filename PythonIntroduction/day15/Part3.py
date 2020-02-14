'''
Created on Feb 14, 2020

@author: bvikram2
'''
'''
Hierarchical Inheritance
'''


class A:

    def methodA(self):
        print("A")


class B(A):

    def methodB(self):
        print("B")

        
class C(A):

    def methodC(self):
        print("C")        

obB = B()
obB.methodA()
obB.methodB()

obC = C()
obC.methodA()
obC.methodC()