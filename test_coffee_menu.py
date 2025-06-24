
import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()

    def tearDown(self):
        self.menu = None

    def test_get_price_Americano(self):
        price = self.menu.get_price("Americano")
        self.assertEqual(price, 2.70)

    def test_get_price_white_tea(self):
        price = self.menu.get_price("White Tea")
        self.assertIsNone(price)

    def test_add_item(self):
        self.menu.add_item("black Chocolate", 3.00)
        self.assertEqual(self.menu.add_item('black Chocolate', 3.00), None)

if __name__ == '__main__':
    unittest.main()