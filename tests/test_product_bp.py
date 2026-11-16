import unittest
from app import app

class ProductBlueprintTestCase(unittest.TestCase):

    def setUp(self):
        """Налаштування клієнта тестування для модуля products."""
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_products_list_page(self):
        """Тест маршруту /products/ (список усіх товарів)."""
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Laptop", response.data)
        self.assertIn(b"Phone", response.data)
        self.assertIn(b"PC", response.data)

    def test_detail_product_page(self):
        """Тест маршруту /products/<id> (детальна інформація про товар)."""
        response = self.client.get("/products/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Laptop", response.data)
        self.assertIn(b"72000", response.data)

    def test_detail_product_not_found(self):
        """Тест маршруту /products/<id> для неіснуючого товару (404)."""
        response = self.client.get("/products/999")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()