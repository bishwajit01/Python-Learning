'''
Created on Jan 30, 2020

@author: Bishwajit.
'''

'''
Set Function
'''
a = {4, 8, 2, 7}

# Sum
print(sum(a))

# Addition
a.add("Bishwajit")
print(a)

# COpy
b = a.copy()
c = a
print(b)
print(c)

# Removing
b.remove(8)
print(b)

# Discard
b.discard(4)
print(b)

# Subset
c = {7, 8, 3, 1, 6, 3, 2}
d = {7, 8}
print(d.issubset(c))

# Union
set1 = {2, 4}
set2 = {1, 0, 4}
print(set1 | set2)
print(set1.union(set2))

# intersection
print(set1.intersection(set2))
print(set1 | set2)

# Difference
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.difference(set1))
print(set1 - set2)

# Frozen Set
# It is immutable
set3 = {1, 2, 3, 4, 5}
set4 = frozenset(set3)
print(set4)
print(type(set4))
