from bson import ObjectId
from pydantic import BaseModel


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema):
        schema.update(type="string")
        return schema


class Customer(BaseModel):
    id: PyObjectId = None
    name: str
    last_name: str
    dni: int
    account_id: int
    balance: float

    class Config:
        populate_by_name = True
        json_encoders = {
            ObjectId: str
        }


class CustomerResponse(BaseModel):
    account_id: int

    class Config:
        from_attributes = True


class CustomersList(BaseModel):
    account_id: int
    balance: float

    class Config:
        from_attributes = True


class CustomerUpdateAccountBalance(BaseModel):
    balance: float
