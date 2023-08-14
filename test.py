from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from config import DB_URL

from hash.model import Salt
from dbmodels import User
# Определите модель данных
Base = declarative_base()

# Создайте объект Engine для подключения к базе данных

engine = create_engine(DB_URL)

# Создайте сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()



def get_passwords(session : Session) -> list[str]:
    passwords = session.query(User.password).all()
    return [password[0] for password in passwords]

# Пример использования
passwds = get_passwords()
print("All passwords:", passwds)