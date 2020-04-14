'''
Created on Feb 14, 2020

@author: Bishwajit.
'''
'''
static variables/class variables
Non-static variables/instance variables
'''


class PythonClass:
    a = 1000

    def methodName(self):
        self.b = 100
        print(self.a)
        print(self.b)
        print(PythonClass.a)
        a = 10
        print(a)

        
ob = PythonClass()
ob.methodName()
# print(ob.a)
