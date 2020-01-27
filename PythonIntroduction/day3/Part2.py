'''
Created on Jan 27, 2020

@author: Bishwajit
'''
'''
String Operations :
1. Indexing
2. SLicing
3. Concatenation
4. Multiplication
'''

a = "apples"

# Indexing
print(a[0])
print(a[3])
print(a[-2])
print(a[4])

# Slicing
print(a[0:3])
print(a[0:-2])
print(a[::-1])
print(a[-1::])
print(a[::])
print(a[0:6:2])

# Concatenation
b = "oranges"
print(a + b)
print(a + b[::-1])

# Multiplication
print(a * 2)
