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
    balance: float

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }


class CustomerResponse(BaseModel):
    dni: int

    class Config:
        orm_mode = True


class CustomersList(BaseModel):
    dni: int
    balance: float

    class Config:
        orm_mode = True


class CustomerUpdateAccountBalance(BaseModel):
    balance: float
