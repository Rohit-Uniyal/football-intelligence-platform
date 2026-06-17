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

try:
    response = s3.list_objects_v2(Bucket=bucket_name)

    print(f"Connected to bucket: {bucket_name}")

    if "Contents" in response:
        print("\nFiles found:\n")

        for obj in response["Contents"]:
            print(obj["Key"])

    else:
        print("Bucket is empty")

except Exception as e:
    print("Error:")
    print(e)