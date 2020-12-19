from pydantic import BaseModel


class ReservaIn(BaseModel):
    username: str

class ReservaOut(BaseModel):
    username:   str
    habitacion: int
    fecha:      str
    comida:     str
    aeropuerto: str
    moredata:   str
    sugerencia: str