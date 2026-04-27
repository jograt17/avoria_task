from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel)
    id: int
    name: str
    sku: str
    price: Decmial
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime