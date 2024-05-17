from typing import List
from fastapi import APIRouter, HTTPException
from app.models.customer import Customer, CustomerResponse, CustomersList, CustomerUpdateAccountBalance
from app.controller.customer import create_account, get_accounts, update_account_balance

router = APIRouter()


@router.post("/accounts", response_model=CustomerResponse, status_code=201)
async def create_customer_endpoint(customer: Customer):
    return await create_account(customer)


@router.get("/accounts", response_model=List[CustomersList], status_code=200)
async def get_accounts():
    return await get_accounts()


@router.put("/accounts/{account_id}", response_model=None, status_code=200)
async def update_account_balance_endpoint(account_id: int, account_balance: CustomerUpdateAccountBalance):
    updated_customer = await update_account_balance(account_id, account_balance.balance)
    if updated_customer is None:
        raise HTTPException(status_code=404, detail='Account not found')

    return {'message': 'Updated account balance'}
