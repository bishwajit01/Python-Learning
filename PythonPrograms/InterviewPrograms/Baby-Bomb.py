'''
Created on Apr 5, 2020

@author: bvikram2
'''
'''
Test cases
==========
Inputs:    (string) M = "2"
           (string) F = "1"
Output:    (string) "1"

Inputs:    (string) M = "4"
           (string) F = "7"
Output:    (string) "4"
'''
def solution(x, y):
    # Your code here
    m, f = int(x), int(y)
    total = 0
    while not (m == 1 and f ==1):
        if f <= 0 and m <= 0:
            return "impossible"
        if f == 1:
            return str(total + m - 1)
        else:
            if f == 0:
                return "impossible"
            total = total + int(m/f)
            m, f = f, m%f
    return str(total)

print(solution(4, 7))