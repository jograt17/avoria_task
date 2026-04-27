from fastapi import APIRouter, Depends, Request, Body
from app.db.database import get_db
from app.service.product_service import ProductService
from app.service.order_service import OrderService
from app.model.product import ProductCreate, ProductUpdate
from app.model.order import OrderRequestModel
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/products")
async def list_products(is_active: bool=None, search: str=None, conn= Depends(get_db)):
    service = ProductService(conn)
    return service.list_products(is_active,search)

@router.post("/products")
async def create_product(body : ProductCreate,conn= Depends(get_db)):
    service = ProductService(conn)
    service.create_product(body)


@router.put("/products/{product_id}")
def update_product(product_id: int, body: ProductUpdate, conn = Depends(get_db)):
    service = ProductService(conn)
    return service.update_product(product_id, body)

@router.post("/orders")
def create_order(order: OrderRequestModel, conn = Depends(get_db)):
    service = OrderService(conn)
    
    return service.create_order(order)