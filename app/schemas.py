from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ItemCreateSchema(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime

class ItemUpdateSchema(BaseModel):
    name: Optional[str]
    email: Optional[str]
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[datetime]
    
class ClockInCreateSchema(BaseModel):
    email: str
    location: str

class ClockInUpdateSchema(BaseModel):
    email: Optional[str]
    location: Optional[str]
