from pydantic import BaseModel, Field
from typing import Optional, Literal
from app.schemas.helpers.core import DateTimeModelMixin

class TransactionBase(BaseModel, DateTimeModelMixin):
    id: Optional[str] = Field(default=None)  
    user_id: str  
    merchant_id: str  
    service_name: str  
    plan_id: str  
    amount: float  
    currency: str = "USDC"  
    status: Literal["pending", "successful", "failed"] = "pending"  
    transaction_hash: Optional[str] = None  

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(BaseModel):
    id: Optional[str] = None
    user_id: str
    merchant_id: str
    service_name: str
    plan_id: str
    amount: float
    currency: str
    status: str
    transaction_hash: Optional[str] = None

    class Config:
        from_attributes = True
