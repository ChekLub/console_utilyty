import json
import urllib.request


url = 'http://ip-api.com/json/'
geoloc = urllib.request.urlopen(url).read().decode()
geoloc = json.loads((geoloc.replace("'", '"')))

lat = geoloc['lat']
lon = geoloc['lon']
region = geoloc['regionName']
""""
print(type(geoloc))
print(geoloc)
print(geoloc['regionName'])
"""

app_id = '90dcc46f'
app_key = 'e16e576ca2c39bdbb28ccac2bdf6ce5a'
url = f"http://api.weatherunlocked.com/api/current/{lat},{lon}?app_id={app_id}&app_key={app_key}"
response = urllib.request.urlopen(url).read()
response = json.loads(response)
wx_desc = response['wx_desc']
temp = response['temp_c']
wind = response['windspd_kmh']
humid = response['humid_pct']
#print(response)

print(f"Погода сейчас в {region}")
print(f"{wx_desc}")
print(f"Температура: {temp} С")
print(f"Ветер: {wind} км/ч")
print(f"Влажность: {humid} %")
