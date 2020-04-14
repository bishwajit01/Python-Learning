'''
Created on Feb 3, 2020

@author: Bishwajit.
'''
'''
Exception Handling Using 
    Try
    Except
    Finally
'''

# try-catch block
a, b = 20, 0
try :
    c = a / b
    print(c)
except:
    print("Error Occurred")

# try-catch block
try :
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Denominator should not be zero")

# try-catch block
a, b = 20, "a"
try :
    c = a / b
    print(c)
except TypeError:
    print("Only Numbers")
 
# try-catch-finally block 
a, b = 20, "a"
try :
    c = a / b
    print(c)
except TypeError:
    print("Only Numbers")
 
