from flask import Flask, request, jsonify
from db import ProductsDB


app = Flask(__name__)
db = ProductsDB('products_db.json')

## view all products
@app.route('/products', methods=['GET'])
def get_all_products():
    """Returns all products in the database"""
    return db.all_products()

# view all product by id
@app.route('/products/id/<id>', methods=['GET'])
def get_all_product(id):
    """Returns product in the database by id"""
    return db.get_product_id(id)

# view all ptoducts names
@app.route('/products/names', methods=['GET'])
def get_product_all_names():
    """Returns all product names"""
    return db.get_all_product_names()


# view products by name
@app.route('/products/name/<name>', methods=['GET'])
def get_products_by_name(name):
    """Returns a product by name"""
    return db.get_names(name)

# view all ptoducts catagories
@app.route('/products/catagories', methods=['GET'])
def get_product_all_catagories():
    """Returns all product catagories"""
    return db.get_all_catagories()

# view products by price
@app.route('/products/price/<price>', methods=['GET'])
def get_products_by_price(price):
    """Returns a product by price"""
    return db.get_small_from_price(price)

# view products expensive
@app.route('/products/price/top/expensive', methods=['GET'])
def get_products_expensive():
    """Returns a top three expensive products"""
    return db.expensive_products()

# view products between max_price and min_price
@app.route('/products/price/between', methods=['GET'])
def get_between_price():
    """Returns a products between max_price and min_price
    get max_price and min_price from query_string
    """
    try:
        min_price = float(request.args.get('min_price', 0))  # Default 0 if not provided
        max_price = float(request.args.get('max_price', float('inf')))  # Default infinity if not provided

        if min_price > max_price:
            return jsonify({"error": "min_price should be less than max_price"}), 400

        products = db.get_between_price(min_price, max_price)  # Ensure this function is safe
        print(f"Database returned: {products}")  # Debugging
        return products
    
    except ValueError:
        return jsonify({"error": "Invalid price values"}), 400
    
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