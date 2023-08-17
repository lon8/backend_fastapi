from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from fastapi import FastAPI
from config import DB_URL, DB_SALT_URL

# --- Внимание! Говнокод

engine = create_engine(DB_URL, connect_args={})

hash_engine = create_engine(DB_SALT_URL, connect_args={})

def connect_db(app : FastAPI) -> Session:
    # Подключение к базе данных
    engine = create_engine(DB_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session

def get_db():
    db = sessionmaker(bind=engine)()
    try:
        yield db
    finally:
        db.close()

def get_salt_db():
    db = sessionmaker(bind=hash_engine)()
    try:
        yield db
    finally:
        db.close()