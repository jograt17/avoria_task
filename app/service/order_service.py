from app.repository.order_repository import OrderRepository
from app.repository.product_repository import ProductRepository
from app.model.order import OrderRequestModel, ProductItemModel
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

class OrderService:
    def __init__(self, conn):
        self.product_repo = ProductRepository(conn)
        self.order_repo = OrderRepository(conn)

    def create_order(self, order: OrderRequestModel):
        # check list of items if still available
        items = order.items
        item_ids = [item.product_id for item in items]
        # retrieve products in one call
        product_items = self.product_repo.get_product_by_ids(item_ids)
        return product_items