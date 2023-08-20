from sqlalchemy.orm import Session
from db.dbmodels import User
import hashlib
import secrets

from db.forms import UserLoginModel
from hash.model import Hash

# Механизм шифрования ->
# 1. Берем user.nickname
# 2. Разворачиваем его
# 3. Используем в качестве соли для предложения
#
# Таким образом каждый hash будет полностью уникальным
# (Такой метод ненадёжен, но пока что так.
# Прекрасно понимаю, что нужно делать с помощью уникальных солей,
# но т.к. это тестовый код, то я решил не заморачиваться)

def reverse_nick(nickname : User.nickname) -> str:
    return nickname[::-1]

def hash_kernel(user : User | UserLoginModel) -> str: # Используем два типа
    data_with_salt = f"{reverse_nick(user.nickname)}{user.password}"
    hashed_data = hashlib.sha256(data_with_salt.encode()).hexdigest()
    return hashed_data

def get_hashes(session : Session) ->list[str]:
    hashes = session.query(Hash.hash).all()
    hash_list = [hash[0] for hash in hashes]
    return hash_list

def verify_hash(user_form : UserLoginModel, hash_from_db : str) -> bool:
    return hash_kernel(user_form) == hash_from_db


#def verify_hash(nickname : str, password : str, hash_from_db):
#    return hash_with_salt(password, reverse_nick(nickname)) == hash_from_db

# Пример использования