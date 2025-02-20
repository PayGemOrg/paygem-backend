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


class PlanUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The updated name of the plan")
    price: Optional[float] = Field(None, gt=0, description="The updated price of the plan")
    billing_cycle: Optional[str] = Field(None, description="The updated billing cycle (e.g., monthly, yearly)")

    class Config:
        schema_extra = {
            "example": {
                "name": "Premium Plan",
                "price": 9.99,
                "billing_cycle": "monthly"
            }
        }
