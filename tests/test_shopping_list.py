import unittest
from module.shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD","Banana", 1.50, 2)
        self.assertEqual(shopping_list.items, 
        [{"barcode": "1234ABCD", "name": "Banana", "price": 1.50,"quantity": 2}])

    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"barcode": "1234ABCD", "name": "Banana", "price": 1.50,"quantity": 2},
            {"barcode": "5678EFGH", "name": "Milk", "price": 2.50,"quantity": 1},
            {"barcode": "9012IJKL", "name": "Bread", "price": 1.00,"quantity": 3},
            {"barcode": "3456MNOP", "name": "Eggs", "price": 3.50,"quantity": 4},
            {"barcode": "7890QRST", "name": "Cheese", "price": 4.50,"quantity": 5}]

        shopping_list.add_multiple_items(list_of_items)
        self.assertEqual(shopping_list.items, list_of_items)

    def test_remove_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD","Banana", 1.50, 2)
        shopping_list.add_item("5678EFGH","Milk", 2.50, 1)
        shopping_list.add_item("9012IJKL","Bread", 1.00, 3)
        shopping_list.add_item("3456MNOP","Eggs", 3.50, 4)
        shopping_list.add_item("7890QRST","Cheese", 4.50, 5)

        shopping_list.remove_item("5678EFGH")
        self.assertEqual(shopping_list.items, 
        [{"barcode": "1234ABCD", "name": "Banana", "price": 1.50,"quantity": 2},
        {"barcode": "9012IJKL", "name": "Bread", "price": 1.00,"quantity": 3},
        {"barcode": "3456MNOP", "name": "Eggs", "price": 3.50,"quantity": 4},
        {"barcode": "7890QRST", "name": "Cheese", "price": 4.50,"quantity": 5}])

    def test_is_valid_barcode(self):
        valid_barcodes = ["1234ABCD", "5678EFGH", "9012IJKL", "3456MNOP", "7890QRST"]
        invalid_barcodes = ["", " ", "1234", "ABCD23", "1234ABCD1", "1234ABCD1@", "1234ABCD12A"]

        for barcode in valid_barcodes:
            self.assertTrue(ShoppingList.is_valid_barcode(self, barcode))

        for barcode in invalid_barcodes:
            self.assertFalse(ShoppingList.is_valid_barcode(self, barcode))