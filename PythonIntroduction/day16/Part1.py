'''
Created on Feb 18, 2020

@author: Bishwajit.
'''
'''
Polymorphism :: One Name Different forms.
    Overloading
        Python doesnot supports overloading
        Here only the paramemter list will vary.
        Only the last method will be taken, rest all will be discarded
        
    Overriding
'''

'''
OverLoading
'''


class A:

    def method1(self):
        print("Empty")

    def method1(self, a):
        print("A")

    def method1(self, a, b):
        print("A, B")


a = A()
# a.method1() # wont execute 

a.method1(3, 8)

