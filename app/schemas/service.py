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

class ServiceUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The updated name of the service")
    description: Optional[str] = Field(None, description="The updated description of the service")
    tags: Optional[str] = Field(None, description="The updated tags for the service")

    class Config:
        schema_extra = {
            "example": {
                "name": "Crypto Streaming Service",
                "description": "A Web3 streaming platform for movies and shows",
                "tags": "streaming, movies, blockchain"
            }
        }

