import random
from typing import List

from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorCursor, AsyncIOMotorCollection
from app.db.database import collection
from app.schemas.customer import AccountCustomerModel, CreateAccountCustomerInput, CreateAccountCustomerResponse, GetAccountCustomersListResponse, UpdateAccountBalanceCustomerInput, CustomerMessageResponse


async def create_account(customer: CreateAccountCustomerInput, connection_database=None) -> CreateAccountCustomerResponse:
    try:
        global collection
        account_id = str(random.randint(10000, 99999))

        if connection_database is not None:
            account_id = 'TEST'
            collection = connection_database

        customer_dict = AccountCustomerModel(
            name=customer.name,
            last_name=customer.last_name,
            dni=customer.dni,
            account_id=account_id,
            balance=0
        )
        await collection.insert_one(customer_dict.dict())
        return CreateAccountCustomerResponse(account_id=account_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_accounts(connection_database: AsyncIOMotorCollection = None) -> List[GetAccountCustomersListResponse]:
    try:
        global collection

        if connection_database is not None:
            collection = connection_database
            accounts = collection.find()
        else:
            cursor: AsyncIOMotorCursor = collection.find()
            accounts = await cursor.to_list(None)

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
        raise HTTPException(status_code=500, detail=str(e))


async def update_account_balance(customer: UpdateAccountBalanceCustomerInput, connection_database=None) -> CustomerMessageResponse:
    try:
        global collection

        if connection_database is not None:
            collection = connection_database

        customer_account = await collection.find_one({'account_id': customer.account_id})
        if customer_account is None:
            raise HTTPException(
                status_code=404, detail='The account not found')

        current_balance = customer_account.get('balance', 0)
        new_balance = current_balance + customer.balance
        balance_updated = await collection.update_one({'account_id': customer.account_id}, {"$set": {"balance": new_balance}})

        if balance_updated.modified_count == 0:
            raise HTTPException(
                status_code=404, detail='The account balance has not been updated or account not found')

        return CustomerMessageResponse(message='The account balance has been updated')

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
