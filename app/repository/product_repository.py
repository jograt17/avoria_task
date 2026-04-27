from app.repository.product_repository_query import ProductRepositoryQuery
from app.model.product import ProductCreate
from psycopg2 import Error as database_error
from fastapi import HTTPException
import logging
logger = logging.getLogger(__name__)

class ProductRepository:
    def __init__(self, conn):
        self.conn = conn
        self.product_query= ProductRepositoryQuery()

    def list_products(self,is_active, search):
        try:
            cur = self.conn.cursor()
            cur.execute(self.product_query.list_products_query(is_active, search))
            rows = cur.fetchall()
            cur.close()
            return rows
        except database_error:
            logger.error("Database error occured")
            raise HTTPException(status_code=500, detail="Database Error")

     
    def create_product(self, product_create:ProductCreate):
        try:
            cur = self.conn.cursor()
            params =  self.product_query.create_product_params(product_create)
            query = self.product_query.create_product_query()
            cur.execute(query, params)
            print(cur.mogrify(query,params))
            rows = cur.fetchall()
            cur.close()
            self.conn.commit()
            return rows[0]
        except database_error:
            self.conn.rollback()
            logger.error("Database error occured")
            raise HTTPException(status_code=500, detail="Database Error")

        
    def get_product_by_id(self, product_id):
        try:
            cur = self.conn.cursor()
            query = self.product_query.get_product_by_id()
            cur.execute(query,(product_id ,))
            print(cur.mogrify(query,(product_id,)))
            row = cur.fetchone()
            cur.close()
            return row
        except database_error:
            self.conn.rollback()
            logger.error("Database error occured")
            raise HTTPException(status_code=500, detail="Database Error")
        

    def update_product(self, product_id: int, body):
        params = {}
        update_product = body.model_dump(exclude_none=True)

        if not update_product:
            return {"message": "No fields to update"}

        params = self.product_query.update_product_params(update_product)
        
        print("PARAMS:", params)
        print(update_product)
        params["id"] = product_id
        query = self.product_query.update_product_query(update_product)

        print("QUERY:", query)

        cur = self.conn.cursor()

        # print("MOGRIFY:", cur.mogrify(query, params))
        cur.execute(query, params)
        updated = cur.fetchone()
        self.conn.commit()
        cur.close()

        return {"updated_id": updated[0]}



    def get_product_by_ids(self, product_ids):
        try:
            cur = self.conn.cursor()
            query = self.product_query.get_product_by_id()
            print("i am", type(tuple(product_ids)))
            print(cur.mogrify(query,product_ids))
            cur.execute(query,product_ids)
            row = cur.fetchone()
            cur.close()
            return row
        except database_error:
            self.conn.rollback()
            logger.error("Database error occured")
            raise HTTPException(status_code=500, detail="Database Error")