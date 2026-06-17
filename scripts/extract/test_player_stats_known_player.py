import requests
import json

API_KEY = "bc501b0689mshf5ce98ab7654ca0p1c20e9jsnefa0ddb895bb"

url = "https://espn-football-soccer.p.rapidapi.com/player-stats/169532"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "espn-football-soccer.p.rapidapi.com"
}

response = requests.get(
    url,
    headers=headers
)

print("Status:", response.status_code)

try:
    data = response.json()
    print(json.dumps(data, indent=2)[:5000])

except:
    print(response.text)