import requests

api_key = "c289713b02792ff7045dfc5693fbaca9"
user_placename = input("Anna paikkakunta: ")

weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={user_placename}&appid={api_key}&units=metric"
weather_call = requests.get(weather_url).json()

print(f"Valittu paikkakunta: {user_placename}")
print(f"Säätila: {weather_call['weather'][0]['description']}") #säätilan teksti
print(f"Lämpötila: {weather_call['main']['temp']}C") #lämpötila
