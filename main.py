from db.usuarios_db import UserInDB
from db.usuarios_db import update_user, get_user 
from models.usuarios_models import UserIn, UserOut
from fastapi import FastAPI
from fastapi import HTTPException
from typing import Dict


app = FastAPI()

@app.post("/user/auth/")
async def auth_s(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        return  {"Autenticado": False}

    return  {"Autenticado": True}
    

@app.get("/user/tipocuenta/{username}")
async def get_cuenta(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

