from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from app.schemas.helpers.core import DateTimeModelMixin

class PlanBase(BaseModel, DateTimeModelMixin):
    id: Optional[str] = Field(default=None)
    service_id: str
    merchant_id: str
    name: str  
    description: Optional[str] = None  
    price: float
    currency: str = "ETH"
    billing_cycle: Literal["monthly", "yearly"] = "monthly"
    features: List[str] = []
    is_active: bool = True
    subscribers_limit: Optional[int] = None
    subscriber_count: Optional[int] = 0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class PlanCreate(PlanBase):
    pass

class PlanResponse(BaseModel):
    id: Optional[str] = None
    service_id: str
    merchant_id: str
    name: str
    description: Optional[str] = None
    price: float
    currency: str
    billing_cycle: str
    features: List[str]
    is_active: bool
    subscriber_count: Optional[int]

    class Config:
        from_attributes = True
