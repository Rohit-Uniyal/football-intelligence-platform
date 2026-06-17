import requests

API_KEY = "bc501b0689mshf5ce98ab7654ca0p1c20e9jsnefa0ddb895bb"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "espn-football-soccer.p.rapidapi.com"
}

leagues = {
    "Premier League": "eng.1",
    "La Liga": "esp.1",
    "Bundesliga": "ger.1",
    "Serie A": "ita.1",
    "Ligue 1": "fra.1",
    "Eredivisie": "ned.1",
    "Portuguese Liga": "por.1",
    "J League": "jpn.1",
    "Argentine Primera": "arg.1",
    "MLS": "usa.1",
    "Brazil Serie A": "bra.1",
    "Saudi Pro League": "ksa.1"
}

for league_name, league_id in leagues.items():

    url = "https://espn-football-soccer.p.rapidapi.com/team-list"

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

    print(f"\n{league_name}")
    print(f"League ID: {league_id}")
    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        try:
            data = response.json()

            teams = (
                data["sports"][0]
                ["leagues"][0]
                ["teams"]
            )

            print(f"Teams Found: {len(teams)}")

        except Exception as e:
            print("Response structure changed")
            print(e)

    else:
        print("League not found")