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
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Account(BaseModel):
    id: PyObjectId = None
    name: str
    last_name: str
    dni: int
    amount: float

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "Wolfang",
                "last_name": "Herrera",
                "dni": 1001222555,
                "amount": 1000000
            }
        }
