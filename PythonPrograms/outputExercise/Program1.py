'''
Created on Feb 4, 2020

@author: Bishwajit.
'''

x = "abcdef"
i = "f"
while i in x:
    x = x[1:]
    print(i, end=" ")

'''
Output ::
f f f f f f
'''
