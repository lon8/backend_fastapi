from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from fastapi import FastAPI, HTTPException
from config import DB_URL, DB_SALT_URL

from db.dbmodels import User

# --- Внимание! Говнокод

engine = create_engine(DB_URL, connect_args={})

hash_engine = create_engine(DB_SALT_URL, connect_args={})

def connect_db(app : FastAPI) -> Session:
    # Подключение к базе данных
    engine = create_engine(DB_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session

def check_user_by_username(username: str, session : Session):
    user_from_db = session.query(User).filter_by(username=username).first()
    
    if user_from_db:
        pass
    else:
        raise HTTPException(status_code=404, detail=f"User with username '{username}' not found")


def get_db():
    db = sessionmaker(bind=engine)()
    try:
        yield db
    finally:
        db.close()

def get_hash_db():
    db = sessionmaker(bind=hash_engine)()
    try:
        yield db
    finally:
        db.close()