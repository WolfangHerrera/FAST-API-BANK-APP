from typing import Optional
from pydantic import BaseModel


class AccountCustomerModel(BaseModel):
    name: str
    last_name: str
    dni: int
    account_id: str
    balance: float


class CreateAccountCustomerInput(BaseModel):
    name: str
    last_name: str
    dni: int


class CreateAccountCustomerResponse(BaseModel):
    account_id: str


class GetAccountCustomersListResponse(BaseModel):
    account_id: str
    balance: float


class UpdateAccountBalanceCustomerInput(BaseModel):
    account_id: Optional[str] = ''
    balance: float


class CustomerMessageResponse(BaseModel):
    message: str
