from typing import List
from app.db.database import db
from app.models.customer import Customer
from pymongo.errors import DuplicateKeyError

from app.schemas.customer import CustomerResponse


async def create_account(customer: Customer) -> Customer:
    existing_customer = await db.accounts.find_one({'dni': customer.dni})
    if existing_customer:
        raise ValueError('Customer already has a account.')

    customer_dict = customer.dict()
    customer_dict.pop('id', None)

    try:
        await db.accounts.insert_one(customer_dict)
    except DuplicateKeyError:
        raise ValueError('Customer already has a account.')

    created_customer = await db.accounts.find_one({'dni': customer.dni})
    return CustomerResponse(**created_customer)


async def get_accounts() -> List[Customer]:
    customers = await db.accounts.find().to_list(length=None)
    return [Customer(**customer) for customer in customers]


async def update_account_balance(account_id: int, new_account_balance: float) -> Customer:
    result = await db.accounts.update_one({'dni': account_id}, {"$set": {"balance": new_account_balance}})
    if result.modified_count == 0:
        return None

    updated_account_balance = await db.accounts.find_one({"dni": account_id})
    return Customer(**updated_account_balance)
