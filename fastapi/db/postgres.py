import os
from dotenv import load_dotenv
import psycopg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

load_dotenv()

def get_connection():
    user = os.getenv("POSTGRES_USER", "admin")
    password = os.getenv("POSTGRES_PASSWORD", "admin")
    dbname = os.getenv("POSTGRES_DB", "fastapi_db")
    host = os.getenv("POSTGRES_HOST", "postgres")

    conn = psycopg.connect(
        user=user,
        password=password,
        dbname=dbname,
        host=host,
    )

    conn.isolation_level = psycopg.IsolationLevel.READ_COMMITTED
    return conn

def get_cursor(conn):
    return conn.cursor()

def get_connection_url():
    user = os.getenv("POSTGRES_USER", "admin")
    password = os.getenv("POSTGRES_PASSWORD", "admin")
    dbname = os.getenv("POSTGRES_DB", "fastapi_db")
    host = os.getenv("POSTGRES_HOST", "postgres")
    
    return f"postgresql+psycopg://{user}:{password}@{host}/{dbname}"

def get_engine():
    DATABASE_URL = get_connection_url()
    engine = create_engine(DATABASE_URL)
    return engine

def get_session_local():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal

def init_db():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)