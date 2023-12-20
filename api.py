import requests
import os
import json

def temperature(zipCode):
    apiKey = str(os.getenv("TOMORROW_IO_API_KEY"))
    url = "https://api.tomorrow.io/v4/timelines?location="+ str(zipCode) +"&fields=temperature&timesteps=1h&units=metric&apikey="+ apiKey
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(url)
    data = json.loads(response.text)
    if 'data' in data:
        temperature = data["data"]["values"]["temperature"]
        return temperature
    else:
        return "Data not available"
def dewPoint(location):
    apiKey = str(os.getenv("TOMORROW_IO_API_KEY"))
    url = "https://api.tomorrow.io/v4/weather/realtime?location="+ str(location) +"&apikey=" + apiKey
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if 'data' in data:
        dewPoint = data["data"]["values"]["dewPoint"]
        return dewPoint
    else:
        return "Data not available"

def windSpeed(location):
    apiKey = str(os.getenv("TOMORROW_IO_API_KEY"))
    url = "https://api.tomorrow.io/v4/weather/realtime?location="+ str(location) +"&apikey=" + apiKey
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if 'data' in data:
        kmph = data["data"]["values"]["windSpeed"]
        mph=int(kmph)*0.621371
        return int(mph)
    else:
        return "Data not available"

def place(zipCode):
    apiKey = str(os.getenv("ZIPCODE_API_KEY"))
    url = "https://app.zipcodebase.com/api/v1/search?apikey="+ apiKey +"&codes="+ str(zipCode) +"&country=US"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(url)
    data = json.loads(response.text)
    city = data["results"][str(zipCode)][0]["city"]
    state = data["results"][str(zipCode)][0]["state"]
    return (city + ", " + state)