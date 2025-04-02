import requests, json
BASE_URL = "https://www.weatherapi.com/docs/"
CITY = "New Delhi"
API_KEY = "YOUR API_KEY"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp']
    temp_feel_like = main['feels_like']
    humidity = main['humidity']
    pressure = main['pressure']
    weather_report = data['weather']
    wind_report = data['wind']
    print(f"{CITY:-^35}")
    print(f"City ID: {data['id']}")
    print(f"Temperature: {temperature}")
    print(f"Feel Like: {temp_feel_like}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {weather_report[0]['description']}")
    print(f"Wind Speed: {wind_report['speed']}")
    print(f"Time Zone: {data['timezone']}")
else:
    print("Error in the HTTP request")
