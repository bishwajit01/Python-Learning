'''
Created on Mar 30, 2020

@author: Bishwajit.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as pl


uri = "https://www.worldometers.info/coronavirus/"
req = requests.get(uri)

print(req)

html = req.text
soup = BeautifulSoup(html,'html.parser')
titleCorona = soup.title
print(titleCorona)
print(titleCorona.text)
print()

liveData = soup.find_all("div", id="maincounter-wrap")
for i in liveData:
    print(i.text)

tableBody = soup.find("tbody")
tableRows = tableBody.find_all("tr")


countries = []
totalCases = []
newCases = []
totalDeath = []
newDeath = []
totalRecovered = []

for i in tableRows:
    td = i.find_all("td")
    countries.append(td[0].text)
    totalCases.append(td[1].text)
    newCases.append(td[2].text)
    totalDeath.append(td[3].text)
    newDeath.append(td[4].text)
    totalRecovered.append(td[5].text)
    
headers = ["Countries", "Total Cases", "New Cases", "Total Death", "New Death", "Total Recovered"]
prepared_list = list(zip(countries, totalCases, newCases, totalDeath, newDeath, totalRecovered))
del prepared_list[:8]
#print(prepared_list)

dataFrames = pd.DataFrame(prepared_list, columns=headers)

dataFrames.to_csv("C:\\Users\\bvikram2\\Desktop\\data.csv", index=False)
print("==========Writing to a file Done==================")

print("***********Reading from File**************")
dataFrame = pd.read_csv("C:\\Users\\bvikram2\\Desktop\\data.csv")

print(dataFrame)

print("***********Reading Top 5 from File**************")
print(dataFrame.head())
print("***********Reading Last 5 from File**************")
print(dataFrame.tail())

newData = dataFrame[0:10]
countries = newData["Countries"]
print("***********COUNTRIES************")
print(countries)
x = list(countries)
totalCase = newData["Total Cases"]
print("***********TOTAL CASES************")
print(totalCase)
y = list(totalCase)

print("***********PLOTTING THE BAR-GRAPHS************")
pl.bar(x[::-1],y[::-1])
pl.xlabel("Countries")
pl.ylabel("TOTAL CASE")
pl.title("CORONA TRACKER")
pl.xticks(rotation=60)

print("***********PLOTTING THE SCATTERED-GRAPHS************")
pl.scatter(x[::-1],y[::-1])
pl.xlabel("Countries")
pl.ylabel("TOTAL CASE")
pl.title("CORONA TRACKER")
