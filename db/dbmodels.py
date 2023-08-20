from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from enum import Enum
import datetime
from config import DB_URL

# --- Class for Stream.status

class StatusStates(Enum): #
    PLANED = 'planed'
    ACTIVE = 'active'
    CLOSED = 'closed'

# --- Models

engine = create_engine(DB_URL, connect_args={})

Base = declarative_base()

class AuthToken(Base): # Token Model
    __tablename__ = 'authtokens'

    id = Column(Integer, primary_key=True)
    token = Column(String(256))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(String(256), default=datetime.datetime.utcnow())


class User(Base): # User Model
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email : str = Column(String(256))
    firstname = Column(String(256))
    lastname = Column(String(256))
    nickname = Column(String(256))
    

class Stream(Base): # Stream Model
    __tablename__ = 'stream'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(256))
    topic = Column(String(256))
    status = Column(String(256), default=StatusStates.PLANED.value)

Base.metadata.create_all(bind=engine)