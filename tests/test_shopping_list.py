import unittest
from module.shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "milk", 2, 1.5)
        self.assertEqual(shopping_list.items, 
        [{"barecode": "1234ABCD", "name": "milk", "quantity": 2, "price": 1.5}])

    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"barecode": "1234ABCD", "name": "milk", "quantity": 2, "price": 1.5},
            {"barecode": "5678EFGH", "name": "bread", "quantity": 1, "price": 1.0},
            {"barecode": "9012IJKL", "name": "eggs", "quantity": 3, "price": 2.0},
            {"barecode": "3456MNOP", "name": "butter", "quantity": 1, "price": 1.5}
            ]

    def test_remove_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD", "milk", 2, 1.5)
        shopping_list.add_item("5678EFGH", "bread", 1, 1.0)
        shopping_list.remove_item("1234ABCD")
        self.assertEqual(shopping_list.items, 
        [{"barecode": "5678EFGH", "name": "bread", "quantity": 1, "price": 1.0}])

    def test_is_valid_barecode(self):
        valid_barecodes = ["1234ABCD", "5678EFGH", "9012IJKL", "3456MNOP"]
        invalid_barecodes = ["", "123", "1234", "12345@", "123456", "1234ABC", "1234ABCD1", "1234ABCD12", "1234ABCD123", "1234ABCD1234"]

        for valid_barecode in valid_barecodes:
            self.assertTrue(ShoppingList.is_valid_barecode(self, valid_barecode))
        
        for invalid_barecodes in invalid_barecodes:
            self.assertFalse(ShoppingList.is_valid_barecode(self, invalid_barecodes))