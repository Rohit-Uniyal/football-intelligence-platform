import requests
import json

url = "https://espn-football-soccer.p.rapidapi.com/team-roster"

headers = {
    "x-rapidapi-key": "bc501b0689mshf5ce98ab7654ca0p1c20e9jsnefa0ddb895bb",
    "x-rapidapi-host": "espn-football-soccer.p.rapidapi.com"
}

params = {
    "teamId": "359",
    "leagueId": "eng.1",
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

    print("\nPlayer:")
    print(data["athletes"][0]["fullName"])

    print("\nPosition:")
    print(data["athletes"][0]["position"]["displayName"])

    print("\nStatistics:")
    print(json.dumps(
        data["athletes"][0]["statistics"],
        indent=2
    )[:10000])

else:
    print(response.text)