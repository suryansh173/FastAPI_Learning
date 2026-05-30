from pydantic import BaseModel

# What user sends when creating product
class ProductCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# What API sends back (includes id)
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

    class Config:
        orm_mode = True