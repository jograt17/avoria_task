from app.repository.product_repository import ProductRepository

class ProductService:
    def __init__(self, conn):
        self.repo = ProductRepository(conn)

    def list_products(self, is_active=None, search=None):
        return self.repo.list_products(is_active, search)

    def create_product(self):
        self.repo.create_product()