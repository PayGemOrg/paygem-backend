from pydantic import BaseModel, EmailStr, Field, SecretStr
from app.schemas.helpers.pyobjectid import PyObjectId
from app.schemas.helpers.core import DateTimeModelMixin
from typing import Optional, Literal
from bson import ObjectId

class AdminBase(BaseModel, DateTimeModelMixin):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    full_name: str
    auth_provider: Literal["email", "google", "facebook", "github"] = "email"
    provider_id: Optional[str] = None
    is_active: bool = True

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class AdminCreate(AdminBase):
    password: SecretStr


class AdminResponse(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    full_name: str
    auth_provider: str
    is_active: bool

    class Config:
        orm_mode = True
