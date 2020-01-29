'''
Created on Jan 30, 2020

@author: bvikram2
'''

# Nested Tuple
a = (3, 7, True)
b = ("Bishwajit", 6.8)
c = (a, b)
print(c)

# Tuple Packing
a = 10
b = True
c = 7.3
d = "Bishwajit"
tup = (a, b, c, d)
print(tup)

# Tuple Unpacking
w, x, y, z = tup
print(w)
print(x)
print(y)
print(z)