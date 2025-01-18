from pydantic import BaseModel, Field
from typing import Optional, Literal
from app.schemas.helpers.core import DateTimeModelMixin

class SubscriptionBase(BaseModel, DateTimeModelMixin):
    id: Optional[str] = Field(default=None)  
    user_id: str  
    merchant_id: str 
    plan_id: str  
    status: Literal["active", "paused", "canceled"] = "active"
    next_billing_date: Optional[str] = None
    last_payment_date: Optional[str] = None
    auto_top_up: bool = False
    amount: float
    currency: str = "USDC"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


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
