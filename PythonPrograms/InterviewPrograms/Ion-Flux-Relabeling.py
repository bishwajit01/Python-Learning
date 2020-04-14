'''
Created on Apr 1, 2020

@author: Bishwajit.
'''

'''
    Ion-FLux-Relabeling
    
Inputs:
h = 3
q = [7, 3, 5, 1]

Output:
 [-1, 7, 6, 3]

Inputs:
h = 5
q = [19, 14, 28]

Output:
[21, 15, 29]
'''


def solution(h, q):
    # Your code here
    if h < 1 and h > 30:
        raise ValueError('Height not correct')
    if len(q) > 10000 or len(q) < 1:
        raise ValueError('Flux converters list is outside of bound')
    items = (2 ** h) - 1
    array = []
    for i in range(len(q)):
        if q[i] < items and q[i] > 0:
            array.append(find_items(q[i], items, items - 1))
        else:
            array.append(-1)
    return array


def find_items(items, current, diff):
    right_node = current - 1
    left_node = right_node - diff // 2
    if right_node == items or left_node == items:
        return current
    else:
        if items <= left_node:
            return find_items(items, left_node, diff // 2)
        else:
            return find_items(items, right_node, diff // 2)
        
        
print(solution(3, [7, 3, 5, 1]))
