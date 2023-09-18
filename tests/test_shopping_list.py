import unittest
from module.shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("123456AB", "Milk", 2.50, 1)
        self.assertEqual(shopping_list.items, [
            {"barecode": "123456AB", "name": "Milk", "price": 2.50, "quantity": 1}
        ])
     
    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"barecode": "123456AB", "name": "Milk", "price": 2.50, "quantity": 1},
            {"barecode": "12ER56AB", "name": "Bread", "price": 1.50, "quantity": 2},
            {"barecode": "12ER575B", "name": "Eggs", "price": 0.50, "quantity": 3}
        ]

        shopping_list.add_multiple_items(list_of_items)
        self.assertEqual(shopping_list.items, list_of_items)

    def test_is_valid_barecode(self):
        valid_barecodes = ["123456AB", "12ER56AB", "12ER575B"]
        invalid_barecodes = ["123456AB1", "12ER56A", "12ER575?"]

        for barecode in valid_barecodes:
            self.assertTrue(ShoppingList.is_valid_barecode(self, barecode))

        for barecode in invalid_barecodes:
            self.assertFalse(ShoppingList.is_valid_barecode(self, barecode))