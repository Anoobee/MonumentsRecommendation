# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from app.models import Base  # adjust import if needed

# Load environment variables from .env file
load_dotenv()

# Build the DATABASE_URL from env or components
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    user = os.getenv("MYSQL_USER", "travel")
    password = os.getenv("MYSQL_PASSWORD", "travel")
    host = os.getenv("MYSQL_HOST", "127.0.0.1")
    port = os.getenv("MYSQL_PORT", "3307")
    db = os.getenv("MYSQL_DATABASE", "travel")
    DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables if run as a script
if __name__ == "__main__":
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Database tables created.")
