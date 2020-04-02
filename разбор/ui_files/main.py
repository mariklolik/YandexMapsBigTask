from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen
import requests
import sqlite3
geolocator = Nominatim(user_agent="my-application")
lat, long = 0, 0
OPENWEATHER_API_KEY = 'd36cbb8582ff58d572c64ba56aaa0f6d'

while not lat and not long:
    try:
        location = geolocator.geocode("Омск")
        lat, long = location.latitude, location.longitude
    except:
        pass
print(lat, long)
url = f"http://api.openweathermap.org/data/2.5/weather?lat={float(lat)}&lon={float(long)}&appid={OPENWEATHER_API_KEY}"
print(url)
response = urlopen(url)
data = json.loads(response.read())
temp = (data['main']['temp'] - 273.15) #перевод из кельвинов в цельсии
print(data)
print(temp)
print(data['weather'][0]['main'])
icon = data['weather'][0]['icon']
p = requests.get(f'http://openweathermap.org/img/wn/{icon}.png')

out = open('img.png', "wb")

out.write(p.content)

out.close()
cur = sqlite3.connect('data.db')
con = cur.cursor()
data = con.execute('SELECT color FROM clothes').fetchall()
[print(i, elem[0]) for i, elem in enumerate(data)]