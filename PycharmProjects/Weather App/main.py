import requests
import json

City = input('Enter Your City Name Here: \n')

Url = f"https://api.weatherapi.com/v1/current.json?key=5f6289e7bd7443b79d7110340230904&q={City}&aqi=no"

r = requests.get(Url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["location"]["name"])
print(wdic["current"]["temp_c"])
print(wdic["current"]["wind_kph"])
