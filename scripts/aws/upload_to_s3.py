import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

bucket_name = os.getenv("S3_BUCKET")

FILES = [

    ("premier_league", "teams"),
    ("premier_league", "players"),
    ("premier_league", "player_stats"),

    ("la_liga", "teams"),
    ("la_liga", "players"),
    ("la_liga", "player_stats"),

    ("bundesliga", "teams"),
    ("bundesliga", "players"),
    ("bundesliga", "player_stats"),

    ("serie_a", "teams"),
    ("serie_a", "players"),
    ("serie_a", "player_stats"),

    ("ligue_1", "teams"),
    ("ligue_1", "players"),
    ("ligue_1", "player_stats"),

    ("eredivisie", "teams"),
    ("eredivisie", "players"),
    ("eredivisie", "player_stats"),

    ("portuguese_liga", "teams"),
    ("portuguese_liga", "players"),
    ("portuguese_liga", "player_stats"),

    ("mls", "teams"),
    ("mls", "players"),
    ("mls", "player_stats"),

    ("saudi_pro_league", "teams"),
    ("saudi_pro_league", "players"),
    ("saudi_pro_league", "player_stats"),
]

for league, folder in FILES:

    file_name = f"{league}_{folder}.json"

    local_file = (
        f"data/raw/{league}/2025_26/"
        f"{folder}/{file_name}"
    )

    s3_key = (
        f"raw/{league}/2025_26/"
        f"{folder}/{file_name}"
    )

    try:

        s3.upload_file(
            local_file,
            bucket_name,
            s3_key
        )

        print(f"Uploaded: {s3_key}")

    except Exception as e:

        print(f"Failed: {s3_key}")
        print(e)

print("\nAll Uploads Completed")