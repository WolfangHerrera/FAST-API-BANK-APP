from app.db.database import db
from app.models.customer import Customer
from pymongo.errors import DuplicateKeyError


async def create_account(customer: Customer) -> Customer:
    pass
