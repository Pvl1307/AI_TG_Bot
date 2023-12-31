import os
from dotenv import load_dotenv

load_dotenv()

# Tokens
TG_TOKEN = os.getenv("TG_TOKEN")
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

# DataBase
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
