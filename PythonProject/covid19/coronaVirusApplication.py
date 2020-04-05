'''
Created on Mar 30, 2020

@author: bvikram2
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd


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
dataFrames = pd.DataFrame(list(zip(countries, totalCases, newCases, totalDeath, newDeath, totalRecovered)), columns=headers)
print(dataFrames)

dataFrames.to_csv("C:\\Users\\bvikram2\\Desktop\\data.csv", index=False)
print("==========Writing to a file Done==========")

