from pydantic import BaseModel, EmailStr


class Customer(BaseModel):
    name: str
    last_name: str
    dni: int
    amount: str


class CustomerResponse(BaseModel):
    dni: int

    class Config:
        orm_mode = True
