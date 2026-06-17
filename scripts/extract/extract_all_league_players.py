import requests
import json
from pathlib import Path
import time

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

for league_name, league_id in LEAGUES.items():

    print("\n" + "=" * 60)
    print(f"Extracting Players: {league_name}")

    teams_file = (
        f"data/raw/{league_name}/2025_26/teams/"
        f"{league_name}_teams.json"
    )

    with open(
        teams_file,
        "r",
        encoding="utf-8"
    ) as file:
        teams_data = json.load(file)

    teams = teams_data["sports"][0]["leagues"][0]["teams"]

    all_players = []

    for team in teams:

        team_id = team["team"]["id"]
        team_name = team["team"]["displayName"]

        print(f"  {team_name}")

        url = (
            "https://espn-football-soccer.p.rapidapi.com/team-roster"
        )

        params = {
            "teamId": team_id,
            "leagueId": league_id,
            "season": "2025"
        }

        try:

            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=30
            )

            if response.status_code != 200:

                print(
                    f"FAILED: {team_name} "
                    f"Status={response.status_code}"
                )

                continue

            roster = response.json()

            for player in roster.get("athletes", []):

                all_players.append({
                    "team_id": team_id,
                    "team_name": team_name,
                    "player_id": player.get("id"),
                    "player_name": player.get("fullName"),
                    "age": player.get("age"),
                    "position": player.get(
                        "position",
                        {}
                    ).get("displayName"),
                    "jersey": player.get("jersey")
                })

            time.sleep(1)

        except Exception as e:

            print(f"ERROR: {team_name}")
            print(e)

            continue

    print(
        f"\nTotal Players Extracted: "
        f"{len(all_players)}"
    )

    output_file = Path(
        f"data/raw/{league_name}/2025_26/players/"
        f"{league_name}_players.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_players,
            file,
            indent=4
        )

    print(
        f"Saved: {output_file}"
    )

print("\nAll Player Files Extracted Successfully")