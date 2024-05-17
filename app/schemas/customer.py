from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    last_name: str
    dni: int
    balance: str


class CustomerResponse(BaseModel):
    dni: int

    class Config:
        orm_mode = True
