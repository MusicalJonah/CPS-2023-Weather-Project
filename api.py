import requests
import os
import json

def temperature(location):
    api_key = str(os.getenv("TOMORROW_IO_API_KEY"))
    url = "https://api.tomorrow.io/v4/weather/realtime?location="+ str(location) +"&apikey=" + api_key
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    temperature = data["data"]["values"]["temperature"]
    farenheit=temperature*9/5+32
    return int(farenheit)

def place(location):
    api_key = str(os.getenv("TOMORROW_IO_API_KEY"))
    url = "https://api.tomorrow.io/v4/weather/realtime?location="+ str(location) +"&apikey=" + api_key
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    place = data["location"]["name"]
    return place