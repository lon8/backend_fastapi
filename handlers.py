import stat
from fastapi import APIRouter, Body, Depends, HTTPException
from db.forms import UserCreateModel, UserLoginModel
from db.dbfuncs import check_user_by_username, get_db, get_hash_db, get_user_by_username
from db.dbmodels import User
from hash.model import Hash

from sqlalchemy.orm import Session
from hash.hashfuncs import hash_kernel, get_hashes, verify_hash




# --- Handlers

router = APIRouter() # Create router object

# Login handler
@router.post('/api/login', name='user:login')
def login(user_form : UserLoginModel = Body(..., embed=True), db : Session = Depends(get_db), hdb : Session = Depends(get_hash_db)):
    check_user_by_username(user_form.nickname, db)
    hashes = get_hashes(hdb)

    for hash in hashes:
        if verify_hash(user_form, hash):
            HTTPException(status_code=200, detail="Done. You are logged in")
        else:
            HTTPException(status_code=404, detail="Invalid Password")

# Registration handler-
@router.post('/api/register/')
def create_user(user : UserCreateModel, db : Session = Depends(get_db), hdb : Session = Depends(get_hash_db)):
    # Working with hash | Create a salt and push in database
    hash = hash_kernel(user)
    new_hash = Hash(hash=hash)
    hdb.add(new_hash)
    hdb.commit()
    hdb.refresh(new_hash)

    # Warning! In new user we write hash_password, not user.password

    new_user = User(firstname=user.firstname, lastname = user.lastname, email=user.email, nickname=user.nickname, password=hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

#@router.get('/')
#def index():
#    return {'status': 'OK'}