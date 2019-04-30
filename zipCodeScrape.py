import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 
from tabulate import tabulate

zips = []
page = requests.get("https://www.zip-codes.com/city/ga-atlanta.asp")

soup = BeautifulSoup(page.content, 'html.parser')

zip = soup.find(id = 'tblZIP')

#header = zip.find_all('tr')
#print(header[2].text)

for row in zip.find_all('tr'):
	col = row.find_all('td')
	zips.append((col[0].text.strip(), col[1].text.strip(), col[2].text.strip(), col[3].text.strip(), col[4].text.strip()))
	#print(col[2].text.strip())

#print(zips)
df = pd.DataFrame(zips)

print(df.head(10))