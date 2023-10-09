import unittest
from module.shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "Banana", 1.50, 2)
        self.assertEqual(shopping_list.items, [{"barcode": "1234ABCD","name": "Banana","price": 1.50,"quantity": 2}])

    def test_remove_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "Banana", 1.50, 2)
        shopping_list.remove_item("1234ABCD")
        self.assertEqual(shopping_list.items, [])
    
    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"barcode": "1234ABCD","name": "Banana","price": 1.50,"quantity": 2},
            {"barcode": "4567EFGH","name": "Apple","price": 2.50,"quantity": 3},
            {"barcode": "7890IJKL","name": "Orange","price": 3.50,"quantity": 4},
            {"barcode": "9012MNOP","name": "Pineapple","price": 4.50,"quantity": 5},
            {"barcode": "3456QRST","name": "Grapes","price": 5.50,"quantity": 6}
            ]
        shopping_list.add_multiple_items(list_of_items)
        self.assertEqual(shopping_list.items, list_of_items)

    def test_is_valid_barcode(self):
        list_of_valid_barcodes = ["1234ABCD","4567EFGH","7890IJKL","9012MNOP","3456QRST"]
        list_of_invalid_barcodes = ["1234ABCD1","4567EFG","7890IJ%",""," "]
        for barcode in list_of_valid_barcodes:
            self.assertTrue(ShoppingList.is_valid_barcode(self, barcode))
        
        for barcode in list_of_invalid_barcodes:
            self.assertFalse(ShoppingList.is_valid_barcode(self, barcode))
        
