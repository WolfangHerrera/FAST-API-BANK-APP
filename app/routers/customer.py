from typing import List
from fastapi import APIRouter, Path
from app.controller.customer import create_account, get_accounts, update_account_balance
from app.schemas.customer import CreateAccountCustomerInput, CreateAccountCustomerResponse, CustomerMessageResponse, GetAccountCustomersListResponse, UpdateAccountBalanceCustomerInput

router = APIRouter()


@router.post("/accounts", response_model=CreateAccountCustomerResponse, status_code=200)
async def create_customer_endpoint(customer: CreateAccountCustomerInput):
    return await create_account(customer)


@router.get("/accounts", response_model=List[GetAccountCustomersListResponse], status_code=200)
async def get_accounts_endpoint():
    return await get_accounts()


@router.patch("/accounts/{account_id}", response_model=CustomerMessageResponse, status_code=200)
async def update_account_balance_endpoint(customer: UpdateAccountBalanceCustomerInput, account_id: str = Path(...)):
    customer.account_id = account_id
    return await update_account_balance(customer)
