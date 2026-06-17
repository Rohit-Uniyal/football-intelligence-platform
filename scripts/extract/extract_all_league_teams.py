import requests
import json
from pathlib import Path

API_KEY = "bc501b0689mshf5ce98ab7654ca0p1c20e9jsnefa0ddb895bb"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "espn-football-soccer.p.rapidapi.com"
}

LEAGUES = {
    "premier_league": "eng.1",
    "la_liga": "esp.1",
    "bundesliga": "ger.1",
    "serie_a": "ita.1",
    "ligue_1": "fra.1",
    "eredivisie": "ned.1",
    "portuguese_liga": "por.1",
    "mls": "usa.1",
    "saudi_pro_league": "ksa.1"
}

url = "https://espn-football-soccer.p.rapidapi.com/team-list"

for league_name, league_id in LEAGUES.items():

    print(f"\n{'=' * 50}")
    print(f"Extracting: {league_name}")
    print(f"League ID: {league_id}")

    params = {
        "leagueId": league_id,
        "season": "2025",
        "limit": "100"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    print("Status:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        output_path = Path(
            f"data/raw/{league_name}/2025_26/teams/{league_name}_teams.json"
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        teams_count = len(
            data["sports"][0]["leagues"][0]["teams"]
        )

        print(f"Teams Found: {teams_count}")
        print(f"Saved: {output_path}")

    else:

        print(f"Failed: {league_name}")
        print(response.text)

print("\nAll Team Files Extracted Successfully")