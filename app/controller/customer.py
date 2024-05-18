from typing import List, Union
from app.db.database import db
from app.models.customer import Customer, CustomerResponse, CustomerUpdateAccountBalance


async def create_account(customer: Customer) -> Union[CustomerResponse, dict]:
    customer.pop('id', None)

    await db.accounts.insert_one(customer)

    created_customer = await db.accounts.find_one({'account_id': customer.dni})
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
