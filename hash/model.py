from sqlalchemy import Column, String, Integer, create_engine

from sqlalchemy.ext.declarative import declarative_base
from config import DB_HASH_URL


engine = create_engine(DB_HASH_URL, connect_args={})

Base = declarative_base()

class Hash(Base):
	__tablename__ = 'hashes'

	id = Column(Integer, primary_key=True)
	hash = Column(String(256))
	
Base.metadata.create_all(bind=engine)