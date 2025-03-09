from tinydb import TinyDB, Query


class ProductsDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
    
    def brands(self):
        """Returns all brands in the database"""
        return self.db.all()
    
    def get_smartphone_by_brand(self, brand):
        """Returns all products by brand"""
        pass
    
    def get_smartphone_by_name(self, name):
        """Returns a product by name"""
        pass

    def get_smartphone_by_price(self, price):
        """Returns a product by price"""
        pass
    
    def add_smartphone(self, smartphone, brand):
        """Adds a product to the database"""
        pass
    
    def delete_smartphone(self, doc_id, brand):
        """Deletes a product from the database"""
        pass

data = ProductsDB('products.json')
print(data.brands())