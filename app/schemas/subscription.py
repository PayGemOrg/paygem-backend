from pydantic import BaseModel, Field
from typing import Optional, Literal
from app.schemas.helpers.core import DateTimeModelMixin

class SubscriptionBase(BaseModel, DateTimeModelMixin): 
    user_id: str  
    merchant_id: str 
    plan_id: int  
    status: Literal["active", "paused", "canceled"] = "active"
    next_billing_date: Optional[str] = None
    last_payment_date: Optional[str] = None
    auto_top_up: bool = False
    amount: float
    currency: str = "USDC"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class SubscriptionCreate(BaseModel):
    plan_id: int


class SubscriptionResponse(BaseModel):
    id: Optional[str] = None
    user_id: str
    merchant_id: str
    plan_id: int
    status: str
    next_billing_date: Optional[str] = None
    last_payment_date: Optional[str] = None
    auto_top_up: bool
    amount: float
    currency: str

    class Config:
        from_attributes = True

def subscription_helper(subscription):
    return {
        "id": subscription[0],
        "user": subscription[1],
        "plan_id": subscription[2],
        "merchant": subscription[3],
        "next_billing_date": subscription[4],
        "is_active": subscription[5],
        "status": subscription[6],
        "amount": subscription[7]
    }