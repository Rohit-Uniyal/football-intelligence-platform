import os
from dotenv import load_dotenv
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

load_dotenv()

df = pd.read_csv("data/processed/teams_bronze.csv")
df.columns = [col.upper() for col in df.columns]

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

success, nchunks, nrows, _ = write_pandas(
    conn,
    df,
    "TEAMS",
    auto_create_table=False
)

print("Success:", success)
print("Rows Loaded:", nrows)

conn.close()