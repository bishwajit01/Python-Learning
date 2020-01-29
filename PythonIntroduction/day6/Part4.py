'''
Created on Jan 30, 2020

@author: bvikram2
'''
'''
Conversion
    Tuple to List
    List to Tuple
    String to Tuple
    Tuple to String
'''

# Tuple to List
tup = ("abc", 4, True)
list1 = list(tup)
print(list1)
print(type(list1))

# List To Tuple
list1 = [6, True, 4.9]
tup = tuple(list1)
print(tup)
print(type(tup))

# String to Tuple
a = "vikram bishu"
tup = tuple(a)
print(tup)

# Tuple to String
a = "".join(tup)
print(a)