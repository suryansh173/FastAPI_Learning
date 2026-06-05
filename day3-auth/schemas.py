from pydantic import BaseModel

# Product schemas
class ProductCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

    class Config:
        orm_mode = True

# User schemas
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str