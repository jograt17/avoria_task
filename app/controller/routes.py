from fastapi import APIRouter, Depends, Request
from app.db.database import get_db
from app.service.product_service import ProductService

router = APIRouter()

@router.get("/products")
async def list_products(is_active: bool=None, search: str=None, conn= Depends(get_db)):
    service = ProductService(conn)
    return service.list_products(is_active,search)

@router.post("/products")
async def create_product():
    print(is_active, search)
    service = ProductService(conn)
    service.create_products(is_active, search)