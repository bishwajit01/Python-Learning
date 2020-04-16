'''
Created on Apr 16, 2020

@author: Bishwajit.
'''


def unpack(a, b, c, d):
    print(a + d)


x = [1, 2, 3, 4]
unpack(*x)

lst = [[1, 2], [3, 4]]
print(sum(lst, []))

a = [1, 2, 3, 4, 5]
for i in range(1, 5):
    a[i - 1] = a[i]
for i in range(0, 5):
    print(a[i], end=" ")

a = 165
b = sum(list(map(int, str(a))))
print()
print(b)
