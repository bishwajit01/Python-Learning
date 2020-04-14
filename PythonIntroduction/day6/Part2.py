'''
Created on Jan 29, 2020

@author: Bishwajit.
'''
'''
Tuple Functions
'''

a = (31, True, "Bishwajit", 6 + 4j, 1, 4, 3.7, 31, 2, 4)

print(len(a))  # Length of a Tuple
print(a.count(31))

b = (2, 6, 8, 3, 5, 8, 3, 6, 8)
print(max(b))  # Maximum Element in the TUPLE b
print(min(b))  # Minimum Element in the TUPLE b
print(sorted(b))  # Sorted elements in tuples in Ascending Order
print(sorted(b, reverse=True))  # Sorted elements in tuples in Descending Order
print(b)  # This is show sorted does not change the order of the collection.
print(sum(b))  # Sum of all the elements in a collection 
