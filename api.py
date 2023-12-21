import requests
import os
import json

ApiKey = str(os.getenv("WeatherApiKey"))
headers = {"accept": "application/json"}

def temperature(zipCode):
    url = "https://api.weatherapi.com/v1/current.json?key="+ ApiKey +"&q="+ str(zipCode) +"&aqi=no"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    print (data)
    if 'current' in data:
        temperature = data["current"]["temp_f"]
        return temperature
    else:
        return "Data not available"


def windSpeed(zipCode):
    url = "https://api.weatherapi.com/v1/current.json?key="+ ApiKey +"&q="+ str(zipCode) +"&aqi=no"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if 'current' in data:
        mph = data["current"]["wind_mph"]
        return int(mph)
    else:
        return "Data not available"
def place(location):
    url = "https://api.weatherapi.com/v1/current.json?key="+ ApiKey +"&q="+ str(location) +"&aqi=no"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if 'location' in data:
        town = data["location"]["name"]
        state = data["location"]["region"]
        country = data["location"]["country"]
        place = town + ", " + state + ", " + country
        return place
    else:
        return "Data not available"