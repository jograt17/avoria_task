from app.repository.product_repository import ProductRepository
from app.model.product import ProductCreate, ProductUpdate
from fastapi import HTTPException
import logging


logger = logging.getLogger(__name__)

class ProductService:
    def __init__(self, conn):
        self.repo = ProductRepository(conn)

    def list_products(self, is_active=None, search=None):
        # do validation
        # if is_active.lower() not in ['true', 'false']
        return self.repo.list_products(is_active, search)

    def create_product(self, product_create):
        product_id = self.repo.create_product(product_create)
        return product_id

    def update_product(self, id, update_product):
        product = self.repo.get_product_by_id(id)
        logger.info(product)
        if not product:
            raise HTTPException(status_code=404, detail="Item not found")
        pydantic_product = ProductUpdate.model_validate(product)
        data_for_update = update_product.model_dump(exclude_unset=True)
        print(data_for_update)
        return product
