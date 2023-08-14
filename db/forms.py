from pydantic import BaseModel

# --- Forms

class UserLoginModel(BaseModel): # Login form
    email : str
    password : str

class UserCreateModel(BaseModel): # Registration form
    email :str
    firstname : str
    lastname : str
    password : str
    nickname : str
