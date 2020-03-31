'''
Created on Mar 31, 2020

@author: bvikram2
'''
'''
List Comprehension
SYNTAX ::
    [expression for item in list]
'''

# Primitive method
letter = []
for letters in 'human':
    letter.append(letters)
print("Old Way :: ", letter)

# List Comprehension
letter = [letters for letters in 'human']
print("New Way :: ", letter)
print()

# Primitive method
square = [1, 2, 3, 4, 5, 6]
squares = []
for i in square:
    squares.append(i ** 2)
print("Old Way :: ", squares)

# List Comprehension
square = [1, 2, 3, 4, 5, 6]
square = [i ** 2 for i in square]
print("New Way :: ", square)
print()

# Primitive method
number = [1, 2, 3, 4, 5, 6]
even = []
for i in number:
    if i % 2 == 0:
        even.append(i)
print("Old Way :: ", even)

# List Comprehension
number = [1, 2, 3, 4, 5, 6]
even = [x for x in number if x % 2 == 0]
print("New Way :: ", even)
print()

# List Comprehension
celsius = [39.2, 36.5, 37.3, 37.8, -40]
fahrenheit = [((9 * x / 5) + 32) for x in celsius] 
print("New Way :: ", fahrenheit)
print()

# List Comprehension
equal = [(x, y, z) for x in range(0, 10) for y in range(x, 10) for z in range(y, 10) if x ** 2 + y ** 2 == z ** 2]
print("New Way :: ", equal)
print()

# List Comprehension
color = ['red', 'white', 'blue', 'orange', 'yellow', 'spacegray']
thing = ['house', 'car', 'laptop']
color_thing = [(x, y) for x in color for y in thing]
print("New Way :: ", color_thing)
print()

# List Comprehension
string_list = ['1', '2', '3']
number_list = [int(x) for x in string_list]
print("New Way :: ", number_list)
print()
