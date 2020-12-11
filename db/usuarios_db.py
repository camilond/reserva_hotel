from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    tipo_cuenta: str

database_users = Dict[str, UserInDB]
database_users = {

    "admin": UserInDB(**{"username":"admin", 
                        "password":"root",
                        "tipo_cuenta":"administrador"}),

    "trabajador1": UserInDB(**{"username":"Trabajador1",
                                "password":"hotel1",
                                "tipo_cuenta":"trabajador"}),

    "cliente1": UserInDB(**{"username":"Cliente1",
                            "password":"reserva1",
                            "tipo_cuenta":"cliente"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

