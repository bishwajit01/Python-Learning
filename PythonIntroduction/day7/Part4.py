'''
Created on Jan 30, 2020

@author: bvikram2
'''

'''
Dictionary Function
    keys()
    values()
    copy()
    pop()
    clear()
'''

a = {'id':4, 'name':'Bishwajit'}

# Keys
print(a.keys())

# Values
print(a.values())

# copy
print(a)
b = a
c = a.copy()
print(b)
print(c)

# pop
print(c.pop('id'))
print(c)

# clear
c.clear()
print(c)
