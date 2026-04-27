from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal

class Order(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    status: Literal['pending','completed','cancelled'] = 'pending'
    total_amount: int
    created_at: datetime
    updated_at: datetime
    
class ProductItemModel(BaseModel):
    product_id: int
    quantity: int
    
class OrderRequestModel(BaseModel):
    customer_name: str
    customer_email: EmailStr
    items: list[ProductItemModel]
