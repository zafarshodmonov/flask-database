# Generate product data in TinyDB-like JSON structure
import random
import json
import random

# Sample data lists
product_names = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones", "Camera", "Monitor", "Keyboard", "Mouse", "Printer"]
categories = ["electronic", "gadgets", "accessories", "office", "gaming"]
descriptions = [
    "High performance laptop", "Latest model smartphone", "Lightweight and powerful tablet",
    "Advanced smartwatch with fitness tracking", "Noise-canceling headphones", "Professional DSLR camera",
    "4K Ultra HD monitor", "Mechanical keyboard with RGB lighting", "Ergonomic wireless mouse", "All-in-one printer"
]
# Create data dictionary in TinyDB format
tinydb_data = {"_default": {}}

for i in range(1, 101):
    tinydb_data["_default"][str(i)] = {
        "id": i,
        "name": random.choice(product_names),
        "price": round(random.uniform(50, 1000), 2),
        "category": random.choice(categories),
        "description": random.choice(descriptions)
    }

# Save to JSON file
tinydb_file_path = "tinydb_products.json"
with open(tinydb_file_path, "w", encoding="utf-8") as json_file:
    json.dump(tinydb_data, json_file, indent=4, ensure_ascii=False)

tinydb_file_path
