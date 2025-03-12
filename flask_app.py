from flask import Flask, request
from db import ProductsDB


app = Flask(__name__)
db = ProductsDB('products_db.json')

## view all products
@app.route('/products', methods=['GET'])
def get_all_products():
    """Returns all products in the database"""
    return db.all_products()
    pass

# view all product by id
@app.route('/products/id/<id>', methods=['GET'])
def get_all_product(id):
    """Returns product in the database by id"""
    return db.get_product_id(id)
    pass

# view all ptoducts names
@app.route('/products/names', methods=['GET'])
def get_product_all_names():
    """Returns all product names"""
    return db.get_all_product_names()
    pass


# view products by name
@app.route('/products/name/<name>', methods=['GET'])
def get_products_by_name(name):
    """Returns a product by name"""
    return db.get_names(name)
    pass

# view all ptoducts catagories
@app.route('/products/catagories', methods=['GET'])
def get_product_all_catagories():
    """Returns all product catagories"""
    pass

# view products by price
@app.route('/products/price/<price>', methods=['GET'])
def get_products_by_price(price):
    """Returns a product by price"""
    pass

# view products expensive
@app.route('/products/price/top/expensive', methods=['GET'])
def get_products_expensive(price):
    """Returns a top three expensive products"""
    pass

# view products between max_price and min_price
@app.route('/products/price/between', methods=['GET'])
def get_between_price():
    """Returns a products between max_price and min_price
    get max_price and min_price from query_string
    """
    pass

# view add product
@app.route('/products/add', methods=['POST'])
def add_products():
    """Adds a product to the database"""
    if request.method == 'POST':
        data_dict = request.json
        return db.add_product(data_dict)
    else:
        return 'Error'


# view delete product
@app.route('/products/delete/<doc_id>', methods=['DELETE'])
def delete_product(doc_id):
    """Deletes a product from the database"""
    pass


if __name__ == '__main__':
    app.run(debug=True)