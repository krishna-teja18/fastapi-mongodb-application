from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid object id')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Item(BaseModel):
    id: Optional[PyObjectId] = None
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: datetime = datetime.utcnow()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserClockIn(BaseModel):
    id: Optional[PyObjectId] = None
    email: str
    location: str
    insert_datetime: datetime = datetime.utcnow()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
