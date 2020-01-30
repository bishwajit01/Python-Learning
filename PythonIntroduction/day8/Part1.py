'''
Created on Jan 30, 2020

@author: bvikram2
'''
'''
Control Flow Statement
    Condition statements
        If statement
        If else statement
        If elif else statement
        Nested If statement
    Looping Statements
        while
        For
    Transfer Statement.
'''

# CONDITIONAL STATEMENT

a = int(input("Enter a number"))

if a > 0:  # if statement
    if a >= 10:
        print("Greater than 10")
    else:
        print("Positive Number")
elif a == 0:  # elif statement
    print("Equal to Zero")
else:  # else statement
    print("Negative Number")
