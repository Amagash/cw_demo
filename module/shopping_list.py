
import re
class ShoppingList:
    """
    A class that represents a list of items to buy.
    """
    def __init__(self):
        self.items = []

    def add_item(self, barecode, name, price, quantity):
        """
        Adds an item to the list.
        :param str barecode: the item's barecode. 
        It is 8 characters string with only numbers and uppercase letters
        :param str name: the item's name
        :param int quantity: the item's quantity
        :param float price: the item's price
        """
        self.items.append({
            "barecode": barecode,
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def add_multiple_items(self, items):
        """
        Adds multiple items to the list.
        :param list items: a list of items
        """
        for item in items:
            self.add_item(item["barecode"], item["name"], item["price"], item["quantity"])

    def is_valid_barecode(self, barecode):
        """
        Checks if the given barecode is valid with a regular expression.
        :param str barecode: the barecode to check.
        :return: True if the barecode is valid, False otherwise
        """
        return re.match(r"^[A-Z0-9]{8}$", barecode)