import requests
import os
import json

def temperature(location):
    apiKey = str(os.getenv("TOMORROW_IO_API_KEY"))
    url = "https://api.tomorrow.io/v4/weather/realtime?location="+ str(location) +"&apikey=" + apiKey
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    temperature = data["data"]["values"]["temperature"]
    farenheit=temperature*9/5+32
    return int(farenheit)

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