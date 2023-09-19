import unittest
from module.shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "Milk", 1.50, 2)
        self.assertEqual(shopping_list.items, 
        [{"barcode": "1234ABCD", "name": "Milk", "price": 1.50, "quantity": 2}])
    
    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"barcode": "1234ABCD", "name": "Milk", "price": 1.50, "quantity": 2},
            {"barcode": "5678EFGH", "name": "Bread", "price": 1.00, "quantity": 1},
            {"barcode": "9012IJKL", "name": "Eggs", "price": 0.50, "quantity": 3},
            {"barcode": "3456MNOP", "name": "Apples", "price": 0.75, "quantity": 1}
        ]
        for item in list_of_items:
            shopping_list.add_item(item["barcode"], item["name"], item["price"], item["quantity"])
        
        self.assertEqual(shopping_list.items, list_of_items)
    
    def test_remove_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "Milk", 1.50, 2)
        shopping_list.add_item("5678EFGH", "Bread", 1.00, 1)
        shopping_list.add_item("9012IJKL", "Eggs", 0.50, 3)
        shopping_list.add_item("3456MNOP", "Apples", 0.75, 1)
        shopping_list.remove_item("5678EFGH")
        self.assertEqual(shopping_list.items, 
        [{"barcode": "1234ABCD", "name": "Milk", "price": 1.50, "quantity": 2},
        {"barcode": "9012IJKL", "name": "Eggs", "price": 0.50, "quantity": 3},
        {"barcode": "3456MNOP", "name": "Apples", "price": 0.75, "quantity": 1}])

    def test_is_valid_barcode(self):
        valid_barcodes = ["1234ABCD", "5678EFGH", "9012IJKL", "3456MNOP"]
        invalid_barcodes = ["", "1234?", "1234ABCD1", "1234ABCD-", "1234ABCD-1", "1234ABCD1-"]
        for barcode in valid_barcodes:
            self.assertTrue(ShoppingList.is_valid_barcode(self, barcode))
        for barcode in invalid_barcodes:
            self.assertFalse(ShoppingList.is_valid_barcode(self, barcode))