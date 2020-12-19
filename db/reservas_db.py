from typing import Dict
from pydantic import BaseModel


class ReservaInDB(BaseModel):
    username:   str
    habitacion: int
    fecha:      str
    comida:     str
    aeropuerto: str
    moredata:   str
    sugerencia: str

database_reservas = Dict[str, ReservaInDB]
database_reservas = {

    "cliente1": ReservaInDB(**{"username":"cliente1",
                            "habitacion":"101",
                            "fecha":"18/12/2020 - 15/01/2021",
                            "comida": "True",
                            "aeropuerto": "False",
                            "moredata": "Llevo 4 maletas",
                            "sugerencia": "Ninguna por el momento"}),
}

def get_reserva(username: str):
    if username in database_reservas.keys():
        return database_reservas[username]
    else:
        return None
