from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime

class NewUserSchema(BaseModel):
    id: int = Field(ge=1)
    username: str | None = Field(max_length=100) 
    first_name: str | None = Field(max_length=100) 
    last_name: str | None = Field(max_length=100) 
    role: str = Field(max_length=20, default='user')


class UserSchema(BaseModel):
    id: int = Field(ge=1)
    username: str | None = Field(max_length=100) 
    first_name: str | None = Field(max_length=100) 
    last_name: str | None = Field(max_length=100) 
    role: str = Field(max_length=20, default='user')
    is_premium: bool = Field(default=False)
    is_active: bool = Field(default=True)
    is_blocked: bool = Field(default=False)
    deleted_at: datetime | None 
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        extra='ignore', 
        str_strip_whitespace=True, 
        from_attributes=True
    )



# class NewUserSchema(BaseModel):
#     id: int = Field(ge=1)
#     first_name: str = Field(max_length=100)
#     last_name: str | None = Field(default=None, max_length=100)
#     username: str | None = Field(default=None, max_length=100)

#     model_config = ConfigDict(from_attributes=True)

#     @field_validator('first_name')
#     def first_name_is_valid(cls, val: str) -> str:
#         if val is None:
#             return None 
        
#         val = val.strip()

#         if not val:
#             raise ValueError('first or last name must be nor empty')

#         return val

# class UserSchema(NewUserSchema):
#     is_active: bool = Field(default=True)
#     is_blocked: bool = Field(default=False)
#     is_deleted: bool = Field(default=False)
#     last_activity: datetime = Field(default=datetime.now())
#     created_at: datetime = Field(default=datetime.now())

#     model_config = ConfigDict(from_attributes=True, extra='ignore')

# class UserLoginSchema(BaseModel):
#     id: int
#     username: str = Field(max_length=100)
