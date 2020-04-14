'''
Created on Jan 27, 2020

@author: Bishwajit.
'''

'''
String Built-in Functions.
'''

a = "apPles keeps doctor awAy"
aa = "$apPles $keeps doctor awAy$"

print(a.capitalize())  # Only First word CamelCase, rest small.
print(a.title())  # each word CamelCase.
print(a.islower())  # True/False based on case.
print(a.isupper())  # True/False based on case.
print(a.lower())  # Converts to lower case.
print(a.upper())  # Converts to upper case.
print(a.replace("a", "A"))  # Replace the String.
print(a.replace("a", "A", 1))  # Replace the String based on the count.
print(a.count("a"))  # Count the number of Occurrence in a String.
print(len(a))  # Length of String.
print(a.split(" ",))  # Splits the String based on the separator, and return as List.
print(a.split(" ", 2))  # Splits the String based on the separator with the max number of split, return as List.
print(aa.strip("$"))  # Removed the characters from both the end of String.
print(aa.lstrip("$"))  # Removed the special characters from the left Side of the String.
print(aa.rstrip("$"))  # Removed the special characters from the left Side of the String.
print(a.swapcase())  # Swap the case of the String
