'''
Created on Jan 28, 2020

@author: bvikram2
'''

# List Operation
list1 = ["a", 2 , True, 3.6, 2]

print(len(list1))  # Size of the List
print(list1.count(2))  # Number of occurrence of any particular element in the list. 

list1.extend([2, 5])  # add elements at the last of the list.
print(list1)

list1.insert(3, [60, 3])  # Insert an object into list at a given Index.
print(list1)

list1.remove(2)  # removes the first occurrence elements.
print(list1)

list1.pop(4)
print(list1)

list1.reverse()  # Reverses the whole list.
print(list1)

list2 = list1.copy()
print(list2)

list1.clear()  # It makes the list empty.
print(list1)
print(list2)

list1 = [4, 6, 8, 923, 56, 223]
print(max(list1))  # Maximum in the list
print(min(list1))  # Minimum in the list

list1.sort()  # sorts the list in ascending order.
print(list1)

list1.sort(reverse=True)
print(list1)
