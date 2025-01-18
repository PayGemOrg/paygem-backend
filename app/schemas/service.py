from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.helpers.core import DateTimeModelMixin

class ServiceBase(DateTimeModelMixin, BaseModel):
    id: Optional[str] = Field(default=None)  
    merchant_id: str  
    name: str
    description: Optional[str] = None
    is_active: bool = True
    tags: str

    class Config:
        arbitrary_types_allowed = True  

class ServiceCreate(ServiceBase):
    pass

class ServiceResponse(BaseModel):
    id: Optional[str] = None
    merchant_id: str
    name: str
    description: Optional[str] = None
    is_active: bool
    tags: str

    class Config:
        from_attributes = True
