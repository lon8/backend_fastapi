from fastapi import APIRouter, Body, Depends
from forms import UserCreateModel, UserLoginModel
from dbfuncs import get_db, get_salt_db
from dbmodels import User
from hash.model import Salt

from sqlalchemy.orm import Session
from hashfuncs import hash_data



# --- Handlers

router = APIRouter() # Create router object

# Login handler
@router.post('/login', name='user:login')
def login(user_form : UserLoginModel = Body(..., embed=True)):
    

# Registration handler-
@router.post('/users/')
def create_user(user : UserCreateModel, db : Session = Depends(get_db), hdb : Session = Depends(get_salt_db)):
    # Working with hash | Create a salt and push in database
    salt, hash_password = hash_data(user.password)
    new_salt = Salt(salt=salt)
    hdb.add(new_salt)
    hdb.commit()
    hdb.refresh(new_salt)

    # Warning! In new user we write hash_password, not user.password

    new_user = User(firstname=user.firstname, lastname = user.lastname, email=user.email, nickname=user.nickname, password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

#@router.get('/')
#def index():
#    return {'status': 'OK'}