import os
import requests
#from noaa_api_v2 import NOAAData
from noaa_sdk import noaa
import json

key = os.environ.get('WEATHER_API_TOKEN')

n = noaa.NOAA()
#print(n.points_forecast(40.7314, -73.8656, hourly=False))
hourly = n.points_forecast(39.618500, -79.947453, hourly=True)
print(hourly)

with open('hourly.txt', 'w') as outfile:
#with open('C:/Users/Paul/Desktop/hourly.txt', 'w') as outfile:
	json.dump(hourly, outfile)

#curl -H "token:<token>" "url"
#$.ajax({ url:<url>, data:{<data>}, headers:{ token:<token> } })