from app.repository.product_repository_query import ProductRepositoryQuery as queries

class ProductRepository:
    def __init__(self, conn):
        self.conn = conn

    def list_products(self,is_active, search):
        cur = self.conn.cursor()
        cur.execute(queries.list_products_query(is_active, search))
        print(cur.mogrify(queries.list_products_query(is_active, search)))
        rows = cur.fetchall()
        cur.close()
        return rows

    def create_products(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, sku, price , stock_quantity, is_active FROM avoria.products")
        rows = cur.fetchall()
        cur.close()
        return rows