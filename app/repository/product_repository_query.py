
class ProductRepositoryQuery():
    def __init__(self):
        pass
    
    def list_products_query(is_active, search):
        base_query = """
            SELECT id, name, sku, price , stock_quantity, is_active FROM avoria.products
            """   
        where_clause = "WHERE 0 = 0"
        print(is_active, search)
        if is_active is not None:
            where_clause += f" AND is_active = {is_active} "
        if search is not None:
            where_clause += f" AND ( sku ILIKE '%{search}%' OR name ILIKE '%{search}%')"

        return base_query + where_clause