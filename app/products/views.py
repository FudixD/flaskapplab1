from flask import render_template, abort
from . import products_bp

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 72000,
        "content": "Ноутбук Lenovo Legion 5 15AHP11: AMD Ryzen 7 250, NVIDIA GeForce RTX 5050 8GB, 16GB DDR5, 512 SSD"
    },
    {
        "id": 2,
        "name": "Phone",
        "price": 38000,
        "content": "iPhone 16 pro 256GB (Чудовий стан) 100%"
    },
    {
        "id": 3,
        "name": "PC",
        "price": 53000,
        "content": "Персональний комп'ютер ARTLINE Gaming X33WHITE: Intel Core i5-12400F, GeForce RTX 3050 6BG, 16GB DDR4, 1TB SSD"
    }
]

@products_bp.route("/")
def list_products():
    return render_template("products/products.html", products=products, title="Список товарів")

@products_bp.route("/<int:product_id>")
def detail_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product is None:
        abort(404)
    return render_template("products/detail_product.html", product=product, title=product["name"])