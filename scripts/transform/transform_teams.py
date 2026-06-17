import json
import pandas as pd

with open("data/raw/teams.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for item in data["response"]:
    row = {
        "team_id": item["team"]["id"],
        "team_name": item["team"]["name"],
        "team_code": item["team"]["code"],
        "country": item["team"]["country"],
        "founded": item["team"]["founded"],
        "national": item["team"]["national"],
        "logo": item["team"]["logo"],
        "venue_id": item["venue"]["id"],
        "venue_name": item["venue"]["name"],
        "venue_address": item["venue"]["address"],
        "venue_city": item["venue"]["city"],
        "venue_capacity": item["venue"]["capacity"],
        "venue_surface": item["venue"]["surface"],
        "venue_image": item["venue"]["image"]
    }

    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv(
    "data/processed/teams_bronze.csv",
    index=False
)

print(df.head())
print("\nRows:", len(df))
print("\nColumns:", len(df.columns))