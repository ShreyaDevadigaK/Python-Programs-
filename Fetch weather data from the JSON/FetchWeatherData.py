import json
with open('weather_data.json')as w:
    data=json.load(w)
    current_temp=data['main']['temp']
    humidity=data['main']['humdity']
    weather_desc=data['weather'][0]['description']
print(f'Current temperature:{temp}')
print(f'Humidity:{humidity}%')
print(f'weather description:{weather_desc}')
