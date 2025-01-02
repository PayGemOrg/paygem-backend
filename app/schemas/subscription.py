from pydantic import BaseModel, Field
from typing import Optional, Literal
from app.schemas.helpers.core import DateTimeModelMixin
from app.schemas.helpers.pyobjectid import PyObjectId
from bson import ObjectId


class SubscriptionBase(BaseModel, DateTimeModelMixin):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId  
    merchant_id: PyObjectId  
    plan_id: PyObjectId  
    status: Literal["active", "paused", "canceled"] = "active"  
    next_billing_date: Optional[str] = None  
    last_payment_date: Optional[str] = None  
    auto_top_up: bool = False  
    amount: float  
    currency: str = "USDC"  

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class SubscriptionCreate(SubscriptionBase):
    pass  


class SubscriptionResponse(BaseModel):
    id: Optional[str] = None
    user_id: str
    merchant_id: str
    plan_id: str
    status: str
    next_billing_date: Optional[str] = None
    last_payment_date: Optional[str] = None
    auto_top_up: bool
    amount: float
    currency: str

    class Config:
        from_attributes = True
