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
        shopping_list.add_item("Banana", 1, 1.5, "AB123456")
        shopping_list.add_item("Orange", 2, 1.2, "AB1834F6")
        shopping_list.remove_item("Banana")
        self.assertEqual(shopping_list.items, [
            {
                "name": "Orange",
                "quantity": 2,
                "price": 1.2,
                "reference": "AB1834F6"
            }])

    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"name": "Banana", "quantity": 1,"price": 1.5, "reference": "AB123456"},
            {"name": "Orange", "quantity": 2,"price": 1.2, "reference": "AB1834F6"},
            {"name": "Apple", "quantity": 3,"price": 1.1, "reference": "A418C4F4"},
            {"name": "Mango", "quantity": 4,"price": 1.3, "reference": "A418D454"},
            {"name": "Pineapple", "quantity": 5,"price": 1.4, "reference": "A418E4F4"},
            {"name": "Grapes", "quantity": 6,"price": 1.5, "reference": "A418F4F4"},
            ]
        
        shopping_list.add_multiple_items(list_of_items)
        self.assertEqual(shopping_list.items, list_of_items)

    def test_is_valid_reference(self):
        valid_references = [
            "AB123456",
            "AB1834F6",
            "A418C4F4",
            "A418D454"
            ]
        
        # invalide references can be longer or shorter than 8 characters
        # have lowercase letters and contains special characters
        invalid_references = [
            "AB1r3457",
            "AB1234567",
            "AB12345?"
            ]

        for reference in valid_references:
            self.assertTrue(ShoppingList.is_valid_reference(reference))

        for reference in invalid_references:
            self.assertFalse(ShoppingList.is_valid_reference(reference))

