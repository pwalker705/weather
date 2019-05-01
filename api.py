import os
import requests
from noaa_api_v2 import NOAAData

key = os.environ.get('WEATHER_API_TOKEN')

data = NOAAData(key)

#categories = data.data_categories(locationid='FIPS:37', sortfield='name')

#for i in categories:
#    print(i)
#headers = {'token': key}
#r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:13', headers= headers)
#weather_data = data.fetch_data(datasetid='GHCND', locationid='ZIP:26501', startdate='2019-04-28', enddate='2019-04-28', limit=10

#print(categories)



#curl -H "token:<token>" "url"
#$.ajax({ url:<url>, data:{<data>}, headers:{ token:<token> } })