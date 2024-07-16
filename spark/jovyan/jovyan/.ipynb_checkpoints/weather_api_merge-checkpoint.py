import requests

api_key = '467b188c3e2df1f576a59ba0637d05ea'
bbox = '-10.5,49.5,2.1,61.0,10'  # lon-left, lat-bottom, lon-right, lat-top, zoom (zoom level can be adjusted as needed)

url = f'https://api.openweathermap.org/data/2.5/box/city?bbox={bbox}&appid={api_key}'
response = requests.get(url)
data = response.json()

