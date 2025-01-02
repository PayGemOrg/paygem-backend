from pydantic import BaseModel, Field
from typing import Optional, List
from app.schemas.helpers.core import DateTimeModelMixin
from app.schemas.helpers.pyobjectid import PyObjectId
from bson import ObjectId


class ServiceBase(BaseModel, DateTimeModelMixin):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    merchant_id: PyObjectId   
    name: str  
    description: Optional[str] = None  
    is_active: bool = True  
    tags: List[str] = []  

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ServiceCreate(ServiceBase):
    pass


class ServiceResponse(BaseModel):
    id: Optional[str] = None
    merchant_id: str
    name: str
    description: Optional[str] = None
    is_active: bool
    tags: List[str]

    class Config:
        from_attributes = True
