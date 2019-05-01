import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 
import csv

zips = []

with open('cities.csv', mode = 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)	
	for row in csv_reader:
		link = ("https://www.zip-codes.com/city/" + (f'{row["STATE"]}') + '-' + str.replace((f'{row["CITY"]}'), " ", "-") + ".asp")
			
		city = (f'{row["CITY"]}' + ',' + f' {row["STATE"]}')
		page = requests.get(link)
		soup = BeautifulSoup(page.content, 'html.parser')
		zip = soup.find(id = 'tblZIP')
		i = 1
		for row in zip.find_all('tr'):
			col = row.find_all('td')
			if i > 1:
				zips.append((city, col[0].text.strip()[-5:], col[1].text.strip(), col[2].text.strip(), col[3].text.strip()))
			i += 1	
	df = pd.DataFrame(zips)
	df.columns = ['City', 'ZipCode', 'Type', 'County', 'Population']
	zipCodes = df.to_csv(r'zipCode.csv', index =False, header = True)	

