'''
Created on Jan 31, 2020

@author: bvikram2
'''

# NESTED LOOP

# WHILE LOOP
a = 1
while a < 5:
    print(a, " Less than 5")
    a += 1
    
# FOR LOOP
a = "apples"
for i in a:
    print(i, end='')
print()

for i in range(6):
    print(i, end=', ')
print()

for i in range(6, 10):
    print(i, end=', ')
print()

for i in range(6, 10, 2):
    print(i, end=', ')
print()

for i in range(4, -2, -1):
    print(i, end=', ')
