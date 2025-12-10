import os
from dotenv import load_dotenv

load_dotenv()

# Простая конфигурация без классов
POSTGRES_USER = os.getenv("POSTGRES_USER", "feedback_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "feedback_password")
POSTGRES_DB = os.getenv("POSTGRES_DB", "feedback_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"