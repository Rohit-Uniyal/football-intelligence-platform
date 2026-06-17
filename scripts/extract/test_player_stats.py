import requests
import json

url = "https://espn-football-soccer.p.rapidapi.com/player-stats/291281"

headers = {
    "x-rapidapi-key": "bc501b0689mshf5ce98ab7654ca0p1c20e9jsnefa0ddb895bb",
    "x-rapidapi-host": "espn-football-soccer.p.rapidapi.com"
}

params = {
    "season": "2025"
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("\nPlayer Stats Preview:\n")
    print(json.dumps(data, indent=2)[:8000])

else:
    print(response.text)