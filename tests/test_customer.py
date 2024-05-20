from app.schemas.customer import CustomerMessageResponse, GetAccountCustomersListResponse, UpdateAccountBalanceCustomerInput
from app.controller.customer import get_accounts, update_account_balance
from fastapi import HTTPException
import pytest
import mongomock
from unittest.mock import AsyncMock
from app.controller.customer import create_account, get_accounts
from app.utils.mock_data import customers_data
from app.schemas.customer import AccountCustomerModel, CreateAccountCustomerResponse, GetAccountCustomersListResponse


@pytest.fixture
def mongo_client():
    client = mongomock.MongoClient()
    yield client
    client.close()


@pytest.fixture
async def mongo_collection(mongo_client):
    db = mongo_client.test_database
    collection = db.test_collection

    await collection.insert_many(customers_data)
    yield collection


@pytest.fixture
def async_mongo_collection(mongo_collection):
    async_collection = AsyncMock()
    async_collection.insert_one = AsyncMock(return_value=None)
    async_collection.insert_many = AsyncMock(return_value=None)
    async_collection.find_one = AsyncMock(return_value=None)
    return async_collection


@pytest.fixture
def async_mongo_collections():
    return mongomock.MongoClient().db.collection


@pytest.mark.asyncio
async def test_create_account(async_mongo_collection):
    customer_dict = AccountCustomerModel(
        name='Wolfang',
        last_name='Herrera',
        dni=1001444666,
        account_id='TEST',
        balance=0
    )
    customer = await create_account(customer_dict, async_mongo_collection)
    response = CreateAccountCustomerResponse(account_id='TEST')
    assert customer == response


@pytest.mark.asyncio
async def test_get_accounts(async_mongo_collections):
    async_mongo_collections.insert_many(customers_data)
    accounts = await get_accounts(async_mongo_collections)
    expected_accounts = [
        GetAccountCustomersListResponse(account_id='1001', balance=6500000),
        GetAccountCustomersListResponse(account_id='1002', balance=7000000)
    ]
    assert accounts == expected_accounts


async def test_update_account_balance(mongo_collection):
    customer_dict = UpdateAccountBalanceCustomerInput(
        account_id='TEST',
        balance=1000000
    )

    customer = await update_account_balance(customer_dict, mongo_collection)

    response = CustomerMessageResponse(
        message='The account balance has been updated'
    )
    assert customer == response
