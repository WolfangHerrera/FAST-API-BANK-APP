import random
from typing import List

from fastapi import HTTPException
from app.db.database import db
from app.schemas.customer import AccountCustomerModel, CreateAccountCustomerInput, CreateAccountCustomerResponse, GetAccountCustomersListResponse, UpdateAccountBalanceCustomerInput, CustomerMessageResponse


async def create_account(customer: CreateAccountCustomerInput) -> CreateAccountCustomerResponse:
    try:
        account_id = str(random.randint(10000, 99999))
        customer_dict = AccountCustomerModel(
            name=customer.name,
            last_name=customer.last_name,
            dni=customer.dni,
            account_id=account_id,
            balance=0
        )
        await db.accounts.insert_one(customer_dict.model_dump())
        return CreateAccountCustomerResponse(account_id=account_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{str(e)}')


async def get_accounts() -> List[GetAccountCustomersListResponse]:
    try:
        accounts = await db.accounts.find().to_list(length=None)

        if not accounts:
            raise HTTPException(
                status_code=404, detail='The accounts not found')

        accounts_list = []
        for account in accounts:
            accounts_list.append(GetAccountCustomersListResponse(**account))

        return accounts_list

    except HTTPException as http_exc:
        raise http_exc

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{str(e)}')


async def update_account_balance(customer: UpdateAccountBalanceCustomerInput) -> CustomerMessageResponse:
    try:
        customer_account = await db.accounts.find_one({'account_id': customer.account_id})
        if not customer_account:
            raise HTTPException(
                status_code=404, detail='The account not found')

        current_balance = customer_account.get('balance', 0)
        new_balance = current_balance + customer.balance
        balance_updated = await db.accounts.update_one({'account_id': customer.account_id}, {"$set": {"balance": new_balance}})

        if balance_updated.modified_count == 0:
            raise HTTPException(
                status_code=404, detail='The account balance has not been updated or account not found')

        return CustomerMessageResponse(message='The account balance has been updated')

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{str(e)}')
