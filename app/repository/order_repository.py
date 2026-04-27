from app.repository.order_repository_query import OrderRepositoryQuery
# from app.model.product import ProductCreate
from psycopg2 import errors as database_error
from fastapi import HTTPException
import logging
logger = logging.getLogger(__name__)

class OrderRepository:
    def __init__(self, conn):
        self.conn = conn
        self.product_query= OrderRepositoryQuery()
