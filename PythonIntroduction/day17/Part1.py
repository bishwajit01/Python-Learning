'''
Created on Feb 25, 2020

@author: bvikram2
'''
'''
Encapsulation
    This is used for data hiding.
    By making the variable private.
    In python, we can make the variable private using the underscore twice(__)
    we can make the private methods as well, by doing the same way.
'''


class classEncapsulation:
    val = 3
    __value = 9  # making it private

    def encapMethod(self):
        print("Inside encapsulation Method")

    def howToUse(self):
        print(self.__value)

    def modify(self, v):
        self.__value = v

        
a = classEncapsulation()
a.encapMethod()
print(a.val)
# print(a.value) # throws error
a.howToUse()

# modifying the value
a.modify(10)
a.howToUse()
