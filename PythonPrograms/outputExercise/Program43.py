'''
Created on Apr 17, 2020

@author: Bishwajit.
'''
a = [1, 2, 3, 4]
b = [sum(a[0:x + 1]) for x in range(0, len(a))]
print(b)

data = [[[1, 2], [3, 4]], [[5, 6], [7.8]]]
print(data[1][0][0])

lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
print(len(lst1 + lst2))
