import random
from typing import List

from fastapi import HTTPException
from app.db.database import db
from app.schemas.customer import AccountCustomerModel, CreateAccountCustomerInput, GetAccountCustomersListResponse, CustomerMessageResponse


async def create_account(customer: CreateAccountCustomerInput) -> AccountCustomerModel:
    try:
        account_id = str(random.randint(10000, 99999))
        customer_dict = AccountCustomerModel(
            name=customer.name,
            last_name=customer.last_name,
            dni=customer.dni,
            account_id=account_id,
            balance=0
        )
        await db.accounts.insert_one(customer_dict.dict())
        return customer_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{str(e)}')


async def get_accounts() -> List[GetAccountCustomersListResponse]:
    try:
        accounts = await db.accounts.find().to_list(length=None)

        if not accounts:
            raise HTTPException(status_code=404, detail='Accounts not found')

        accounts_list = []
        for account in accounts:
            accounts_list.append(GetAccountCustomersListResponse(**account))

        return accounts_list

    except HTTPException as http_exc:
        raise http_exc

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{str(e)}')

# async def update_account_balance(account_id: int, new_account_balance: float) -> Customer:
#     result = await db.accounts.update_one({'dni': account_id}, {"$set": {"balance": new_account_balance}})
#     if result.modified_count == 0:
#         return None

#     updated_account_balance = await db.accounts.find_one({"dni": account_id})
#     return Customer(**updated_account_balance)
