import json

with open("data/raw/teams.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total Teams:", data["results"])

first_team = data["response"][0]

print("\nTeam Keys:")
print(first_team["team"].keys())

print("\nVenue Keys:")
print(first_team["venue"].keys())
