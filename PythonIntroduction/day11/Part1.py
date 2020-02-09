'''
Created on Feb 9, 2020

@author: bvikram2
'''
'''
Modules
    Group of instructions or function.
    Every python file itself is a module.
    We can use properties of one module into another.
Import
    Normal import
        entire python file or module is imported.
        module name is used to access the properties of that module
        we can create alias name for the module.
    From import
       We can import required properties of a module.
       we access the properties of the module without using the module name. 
Built-in-Module
    Predefined modules in python.
'''
import module1 as mod1
mod1.function1()
print(mod1.a)

from module2 import a
print(a) 

import math
print("SQRT of 10 : ", math.sqrt(100))
