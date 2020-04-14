'''
Created on Feb 18, 2020

@author: Bishwajit.
'''
'''
OverRiding

'''


class Parent:

    def __init__(self):
        print("Parent")

    def cars(self):
        print("Parent car")

    def bike(self):
        print("Parent bike")

        
class Child(Parent):

    def __init__(self):
        print("Child")

    def cars(self):
        print("Child Car");

        
c = Child()
c.cars()
c.bike()
