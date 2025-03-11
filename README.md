# Products Store - Flask App  

## Objective  

This project is a simple web application built with the **Flask framework** and **TinyDB database**, which displays a list of products and their details.  

## Requirements  

- [ ] The home page should display a list of all products.  
- [ ] The app should have a form that allows users to add new products.  
- [ ] The app should allow users to view a product by specifying the following in the URL:  
  - [ ] **Product ID** (`/products/id/<id>`)  
  - [ ] **Product Name** (`/products/name/<name>`)  
  - [ ] **Product Category** (`/products/categories`)  
  - [ ] **Product Price** (`/products/price/<price>`)  

## Database  

This project includes the following product categories:  

- Electronics  
- Home Appliances  
- Toys  
- Books  
- Sports Equipment  

Each product has the following properties:  

- `id` - The unique ID of the product.  
- `name` - The name of the product.  
- `category` - The category to which the product belongs.  
- `price` - The price of the product.  
- `description` - A brief description of the product.  

### **Sample Database Structure**  

```json
{
    "1": {
        "id": 1,
        "name": "Keyboard",
        "category": "gaming",
        "price": 357.57,
        "description": "RGB backlit gaming keyboard"
    }
}
```

## ProductsDB - Database Class  

This project uses a `ProductsDB` class to manage the database. It includes the following methods:  

- `__init__` - Initializes the database.  
- `all_products()` - Returns all products.  
- `get_product_id(id)` - Retrieves a product by its ID.  
- `get_all_product_names()` - Returns all product names.  
- `get_names(name)` - Retrieves products by name.  
- `get_all_categories()` - Returns all product categories.  
- `get_small_from_price(price)` - Returns products cheaper than a given price.  
- `expensive_products()` - Returns the **top three most expensive** products.  
- `get_between_price(max_price, min_price)` - Returns products within a price range.  
- `add_product(product)` - Adds a new product.  
- `delete_product(doc_id)` - Deletes a product by ID.  

## API Endpoints  

### **GET Requests**  
- **`/products`** - Returns a list of all products.  
- **`/products/id/<id>`** - Returns a product by ID.  
- **`/products/names`** - Returns a list of all product names.  
- **`/products/name/<name>`** - Returns a product by name.  
- **`/products/categories`** - Returns all product categories.  
- **`/products/price/<price>`** - Returns products based on a given price.  
- **`/products/price/top/expensive`** - Returns the top three most expensive products.  
- **`/products/price/between?min_price=<min>&max_price=<max>`** - Returns products within a price range.  

### **POST Requests**  
- **`/products/add`** - Adds a new product to the database.  
  - Required JSON data format:  
    ```json
    {
        "name": "Wireless Mouse",
        "category": "electronics",
        "price": 29.99,
        "description": "Wireless optical mouse"
    }
    ```  
- **`/products/delete/<doc_id>`** - Deletes a product by ID.  

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/khakimovallamurod/flask-database.git
   cd flask-database
   ```
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:  
   ```bash
   python app.py
   ```
4. Open your browser and go to:  
   ```
   http://127.0.0.1:5000/
   ```

## Future Improvements  

- Add **user authentication**.  
- Implement **filtering and sorting** for products.  
- Improve **UI design** using Bootstrap or React.  
