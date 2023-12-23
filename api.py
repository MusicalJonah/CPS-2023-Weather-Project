import requests, os, json

ApiKey = str(os.getenv("WeatherApiKey"))
headers = {"accept": "application/json"}

def weather(zipCode):
    url = "https://api.weatherapi.com/v1/current.json?key="+ ApiKey +"&q="+ str(zipCode) +"&aqi=no"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    temperature = data["current"]["temp_f"]
    windSpeed = data["current"]["wind_mph"]
    pressure = data["current"]["pressure_mb"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]
    image = data["current"]["condition"]["icon"]
    town = data["location"]["name"]
    state = data["location"]["region"]
    country = data["location"]["country"]
    location = (town + ", " + state + ", " + country)
    return temperature, windSpeed, pressure, humidity, condition, image, location