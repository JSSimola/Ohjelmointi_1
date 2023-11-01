import requests

url = "https://api.chucknorris.io/jokes/random"
ans = requests.get(url).json()

print(ans.get("value"))
