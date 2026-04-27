
from app.model.product import ProductCreate

class ProductRepositoryQuery():
    def __init__(self):
        pass
    
    def list_products_query(self, is_active, search):
        base_query = """
            SELECT * FROM avoria.products
            """   
        where_clause = "WHERE 0 = 0"
        print(is_active, search)
        if is_active is not None:
            where_clause += f" AND is_active = {is_active} "
        if search is not None:
            where_clause += f" AND ( sku ILIKE '%{search}%' OR name ILIKE '%{search}%')"

        return base_query + where_clause

        
    def create_product_params(self, product_create: ProductCreate):
        return {
            "name": product_create.name,
            "sku": product_create.sku,
            "price": product_create.price,
            "stock_quantity": product_create.stock_quantity
        }

    def create_product_query(self):
        return """
            INSERT INTO avoria.products (name, sku, price, stock_quantity, is_active, created_at, updated_at)
            VALUES(%(name)s, %(sku)s, %(price)s, %(stock_quantity)s, TRUE, now(), now())
            RETURNING id     
        """

    def get_product_by_id(self):
        return  "SELECT * FROM avoria.products WHERE id = %s"
    
    def get_product_by_ids(self):
        return  "SELECT * FROM avoria.products WHERE id  ANY(%s)"


    def update_product_params(self, update_product): 
        params = {}
        for field, value in update_product.items():
            params[field] = value
            
        return params

    def update_product_query(self, update_product):
        set_clauses = []

        for field in update_product.keys():
            set_clauses.append(f"{field} = %({field})s")

        

        base_query = f"""
            UPDATE avoria.products
            SET {', '.join(set_clauses)}
            WHERE id = %(id)s
            RETURNING id
        """
        return base_query