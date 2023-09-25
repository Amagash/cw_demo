import unittest
from module.shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "Banana", 1.50, 2)
        self.assertEqual(shopping_list.items, 
            [{"barcode": "1234ABCD", "name": "Banana", "price": 1.50, "quantity": 2}])

    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"barcode": "1234ABCD", "name": "Banana", "price": 1.50, "quantity": 2},
            {"barcode": "5678EFGH", "name": "Apple", "price": 2.50, "quantity": 1},
            {"barcode": "9012IJKL", "name": "Orange", "price": 0.50, "quantity": 3},
            {"barcode": "3456MNOP", "name": "Pineapple", "price": 3.50, "quantity": 1},
            {"barcode": "7890QRST", "name": "Strawberry", "price": 4.50, "quantity": 2}]
        shopping_list.add_multiple_items(list_of_items)
        self.assertEqual(shopping_list.items, list_of_items)

    def test_remove_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "Banana", 1.50, 2)
        shopping_list.remove_item("1234ABCD")
        self.assertEqual(shopping_list.items, [])

    def test_is_valid_barcode(self):
        valid_barcodes = ["1234ABCD", "5678EFGH", "9012IJKL", "3456MNOP"]
        invalid_barcodes = ["", " ", "1234", "1234ABCD1", "1234ABCD-"]
        for barcode in valid_barcodes:
            self.assertTrue(ShoppingList.is_valid_barcode(self, barcode))
        for barcode in invalid_barcodes:
            self.assertFalse(ShoppingList.is_valid_barcode(self, barcode))