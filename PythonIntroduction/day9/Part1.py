'''
Created on Feb 1, 2020

@author: Bishwajit.
'''

'''
Functions
    Code reusability.
    Group of Statements.
    def keyword describes the function.
    
Types
    Built-in Function
    User Defined Functions
'''


# Function without any parameter
def foo():
    print("Inside foo")


foo()


# Function with parameter
def foo1(name):
    print("Inside foo1:", name)


foo1("Bishwajit")    


# Function within a Function
def foo2():
    print("Inside foo2")
    foo3()


def foo3():
    print("Inside foo3")


def foo4():
    print("Inside foo4")


foo2()


# Function return
def foo5(n):
    print("Inside foo5")
    return n


a = foo5(6)
print(a)
