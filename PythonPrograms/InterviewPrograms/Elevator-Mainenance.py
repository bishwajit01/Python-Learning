'''
Created on Apr 1, 2020

@author: bvikram2
'''
'''
Elevator-Maintenance
Test cases
==========
Inputs:
    (string list) l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
Output:
    (string list) ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

Inputs:
    (string list) l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
Output:
    (string list) ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
'''


def elevator(versions):
    # Your code here
    return sorted(versions, key=lambda versions:[int(i) for i in versions.split('.')])


print(elevator(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))

