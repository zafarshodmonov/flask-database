from tinydb import TinyDB, Query


class ProductsDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        self.table = self.db.table('Products')
    
    def all_products(self):
        """Returns all products in the database"""
        pass
    
    def get_product_id(self, id):
        """Returns all products by id"""
        pass
    
    def get_all_product_names(self):
        """Returns all product names"""
        pass

    def get_names(self, name: str):
        """Returns all products by name"""
        pass

    def get_all_catagories(self):
        """Returns all catagories name"""
        pass
    
    def get_small_from_price(self, price):
        """Returns products if product's price small from price"""
        pass

    def expensive_products(self):
        """Returns a top three expensive products"""
        pass
    
    def get_between_price(self, max_price, min_price):
        """Returns a products between max_price and min_price"""
        pass

    def add_product(self, product):
        """Adds a product to the database"""
        pass

    def delete_product(self, doc_id):
        """Deletes a product from the database"""

