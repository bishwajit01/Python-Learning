'''
Created on Apr 2, 2020

@author: bvikram2
'''

'''
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
