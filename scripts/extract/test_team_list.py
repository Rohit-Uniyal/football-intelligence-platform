import requests

url = "https://espn-football-soccer.p.rapidapi.com/team-list"

headers = {
    "x-rapidapi-key": "bc501b0689mshf5ce98ab7654ca0p1c20e9jsnefa0ddb895bb",
    "x-rapidapi-host": "espn-football-soccer.p.rapidapi.com"
}

params = {
    "leagueId": "eng.1",
    "season": "2025",
    "limit": 20
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

print("Status:", response.status_code)
print(response.text[:3000])