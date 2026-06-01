from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


# Task 1 — Return your name and college
@app.get("/")
def home():
    return {
        "name": "Suryansh Pratap Singh",
        "college": "Jaypee University of Engineering and Technology",
        "message": "FastAPI learning"
    }

# Task 2 — Product by ID (Path Parameter)
@app.get("/product/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": "Sample Product",
        "price": 999,
        "in_stock": True
    }

# Task 3 — Create Product (POST Request)
class Product(BaseModel):
    name: str
    price: float

@app.post("/create-product")
def create_product(product: Product):
    return {
        "message": "Product created successfully!",
        "product_name": product.name,
        "product_price": product.price
    }