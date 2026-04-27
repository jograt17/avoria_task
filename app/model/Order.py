from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class Product(BaseModel)
    id: int
    customer_name: str
    customer_email: str
    status: Literal['pending','completed','cancelled'] = 'pending'
    total_amount: int
    created_at: datetime
    updated_at: datetime
    