from db.usuarios_db import UserInDB
from db.usuarios_db import update_user, get_user 
from models.usuarios_models import UserIn, UserOut
from fastapi import FastAPI
from fastapi import HTTPException
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", https://front-reserva-hotel.herokuapp.com/,
]

app.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

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

