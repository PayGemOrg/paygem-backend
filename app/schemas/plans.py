from pydantic import BaseModel, Field
from typing import Optional, List
from app.schemas.helpers.core import DateTimeModelMixin
from app.schemas.helpers.pyobjectid import PyObjectId
from bson import ObjectId


class PlanBase(BaseModel, DateTimeModelMixin):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    service_id: PyObjectId
    merchant_id: PyObjectId 
    name: str  
    description: Optional[str] = None  
    price: float  
    currency: str = "ETH"  
    billing_cycle: str = "monthly"  
    features: List[str] = []  
    is_active: bool = True 
    subscribers_limit = Optional[int] = None
    subscriberCount = Optional[int] = 0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


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
    subscriberCount = Optional[int]

    class Config:
        from_attributes = True
