'''
Created on Feb 9, 2020

@author: bvikram2
'''
'''
Package
    Group of modules. 
'''

import package.module1
print(package.module1.a)

import package.module1 as pkg1
pkg1.function1()

import package.module2 as pkg2
pkg2.function2()

# calling Subpackage
import package.subPackage.module3
package.subPackage.module3.function3()
