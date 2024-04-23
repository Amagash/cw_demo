import unittest
from module.a_shopping_list import Item

class TestItem(unittest.TestCase):
    def test_validate_id(self):
      valid_ids = ["A1234567", "B7654321","C2345678","D3456789","E4567890"]
      invalid_ids = [
        "A1234567A", # too long
        "A123456", # too short
        "a1234567", # lowercase
        "A123456?", # special caracter
        "A12 4567" # space
      ]
      for id in valid_ids:
        self.assertTrue(Item.validate_id(id))

      for id in invalid_ids:
        self.assertFalse(Item.validate_id(id))
