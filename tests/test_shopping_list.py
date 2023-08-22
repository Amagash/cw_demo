import unittest
from module.shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_init(self):
        shopping_list = ShoppingList()
        self.assertEqual(shopping_list.items, [])

    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("Banana", 1, 1.5)
        self.assertEqual(shopping_list.items, [
            {
                "name": "Banana",
                "quantity": 1,
                "price": 1.5
            }])

    def test_remove_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("Banana", 1, 1.5)
        shopping_list.add_item("Orange", 2, 1.2)
        shopping_list.remove_item("Banana")
        self.assertEqual(shopping_list.items, [
            {
                "name": "Orange",
                "quantity": 2,
                "price": 1.2
            }])

    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"name": "Banana", "quantity": 1,"price": 1.5},
            {"name": "Orange", "quantity": 2,"price": 1.2},
            {"name": "Apple", "quantity": 3,"price": 1.1},
            {"name": "Mango", "quantity": 4,"price": 1.3},
            {"name": "Pineapple", "quantity": 5,"price": 1.4},
            {"name": "Grapes", "quantity": 6,"price": 1.5}
            ]
        
        shopping_list.add_multiple_items(list_of_items)
        self.assertEqual(shopping_list.items, list_of_items)


