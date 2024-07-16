import pandas as pd
import requests

api_key = '35e46a149c7c75c1fda2635f15ba0c4a'
bbox = '-10.5,49.5,2.1,61.0,10'  # lon-left, lat-bottom, lon-right, lat-top, zoom (zoom level can be adjusted as needed)

url = f'https://api.openweathermap.org/data/2.5/box/city?bbox={bbox},10&appid={api_key}'
response = requests.get(url)
data = response.json()

