from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from app.schemas.helpers.core import DateTimeModelMixin

class PlanCreate(BaseModel):
    service_id: int
    name: str
    description: Optional[str] = ""
    price: int
    currency: str = "ETH"
    billing_cycle: Literal["monthly", "yearly"] = "monthly"
    subscribers_limit: Optional[int] = None

class PlanResponse(BaseModel):
    id: Optional[str] = None
    service_id: int
    merchant_id: str
    name: str
    description: Optional[str] = None
    price: int
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

def plan_helper(plan):
    return {
        "id": plan[0],
        "service_id": plan[1],
        "merchant": plan[2],
        "name": plan[3],
        "description": plan[4],
        "price": plan[5],
        "currency": plan[6],
        "billing_cycle": plan[7],
        "is_active": plan[8],
        "subscriber_limit": plan[9],
        "subscriber_count": plan[10]
    }