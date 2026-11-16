import os
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = quote_plus(os.environ["DB_PASSWORD"])
DB_NAME = os.environ["DB_NAME"]

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"

engine = create_engine(DATABASE_URL)
MakeSession = sessionmaker(bind=engine)


def get_db():
    session = MakeSession()
    try:
        yield session
    finally:
        session.close()
