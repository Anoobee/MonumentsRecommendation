# app/create_db.py

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from app.models import Base  # adjust if needed

# Load .env
load_dotenv()

# Get DB URL
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST", "127.0.0.1")
    port = os.getenv("MYSQL_PORT", "3307")
    db = os.getenv("MYSQL_DATABASE")
    DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"

# Create engine and initialize DB
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
