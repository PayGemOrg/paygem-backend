from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from bson import ObjectId
from app.schemas.helpers.core import DateTimeModelMixin
from app.schemas.helpers.pyobjectid import PyObjectId

class MerchantBase(BaseModel, DateTimeModelMixin):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    business_name: str
    email: EmailStr
    wallet_address: str
    claimable_balance: float = 0.0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
