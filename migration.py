import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv("marc.env")

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")


file_path = "raw_data/candidates.csv"  
candidates = pd.read_csv(file_path, delimiter=';')

engine = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

try:
    candidates.to_sql("candidates_clean", engine, if_exists="replace", index=False)
    print("Succesfull migration")
except Exception as e:
    print(f"Error in migration: {e}")

