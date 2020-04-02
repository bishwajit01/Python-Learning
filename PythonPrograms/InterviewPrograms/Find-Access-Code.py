'''
Created on Apr 2, 2020

@author: bvikram2
'''

'''
Find the Access Code

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

Input: [1, 1, 1]
Output: 1

Input: [1, 2, 3, 4, 5, 6]
Output: 3
'''


def solution(l):
    triplet = 0
    pairs = [0] * len(l)
    for i in range(1, len(l) - 1):
        for j in range(i):
            if(l[i] % l[j] == 0):
                pairs[i] += 1
                
    for i in range(2, len(l)):
        for j in range(1, i):
            if(l[i] % l[j] == 0):
                triplet += pairs[j]
    return triplet

    
print(solution([1, 2, 3, 4, 5, 6]))
