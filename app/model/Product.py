from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional


class Product(BaseModel):
    id: int
    name: str
    sku: str
    price: Decimal
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: Decimal
    stock_quantity: int

class ProductList(BaseModel):
    is_active: bool
    search: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[Decimal] = None
    stock_quantity: Optional[int] = None
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
