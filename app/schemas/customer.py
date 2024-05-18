from pydantic import BaseModel


class CreateAccountCustomerInput(BaseModel):
    name: str
    last_name: str
    dni: int


class CreateAccountCustomerResponse(BaseModel):
    account_id: int


class CustomersList(BaseModel):
    account_id: int
    balance: float

    class Config:
        orm_mode = True


class CustomerUpdateAccountBalance(BaseModel):
    balance: float
