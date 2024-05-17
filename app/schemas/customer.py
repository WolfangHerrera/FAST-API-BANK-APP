from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    last_name: str
    dni: int
    balance: float


class CustomerResponse(BaseModel):
    dni: int

    class Config:
        orm_mode = True


class CustomersList(BaseModel):
    dni: int
    balance: float

    class Config:
        orm_mode = True


class CustomerUpdateAccountBalance(BaseModel):
    balance: float
