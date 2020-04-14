'''
Created on Mar 30, 2020

@author: Bishwajit.
'''

'''
MathPlotLib
    Data Visualization in python.
    Installing -- > pip3 install matplotlib
'''

import matplotlib.pyplot as pp

x = [1, 2, 3, 4, 5, 6, 7, 8]
pp.plot(x)  # LINE GRAPH

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 20, 30, 40, 50, 60, 70, 80]
pp.plot(x, y, linewidth=6, color='r')  # LINE GRAPH WITH LINE WIDTH 6 and COLOR RED.

pp.bar(x, y)  # BAR GRAPH

pp.title("First Graph") # TITLE
pp.xlabel("X Values")   # X LABEL
pp.ylabel("Y Values")   # Y LABEL
pp.bar(x, y, color='r') # BAR GRAPH IN RED COLOR
