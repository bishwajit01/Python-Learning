'''
Created on Feb 9, 2020

@author: bvikram2
'''
'''
Modules
    Group of Instruction or function.
    Every Python file itself is a Module.
    We can use properties of one modules into another.
    
Import
    Normal Import
        Entire Python file or module object is imported.
        Module name is used to access the properties of that module.
        We can create alias name for the name for the module.
    From Import
        We can import required properties from a module.
        We can access the properties of that module without using the module name.
        
Built-In-Modules
    Pre-defined modules. Example math
'''

import module1 as mod

mod.function1()
print("Module 1 :: ", mod.a)

from module2 import a
print("Module 1 :: ", a)

import math
print("Square root:: ", math.sqrt(100))
