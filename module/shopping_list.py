import re
class ShoppingList:
    """
    A class to represent a list of items to buy
    """
    def __init__(self):
        """
        Initialize an empty shopping list
        """
        self.items = []

    def add_item(self, barecode, name, quantity, price):
        """
        Add an item to the shopping list
        :param str barecode: the item's barecode. The barecode is a unique 8 
        character string in the list with only numbers and uppercase letters.
        :param str name: the item's name
        :param int quantity: the item's quantity
        :param float price: the item's price
        """
        self.items.append({
            "barecode": barecode,
            "name": name,
            "quantity": quantity,
            "price": price
        })
    
    def add_multiple_items(self, items):
        """
        Add multiple items to the shopping list
        :param list items: a list of items to add to the shopping list
        """
        for item in items:
            self.add_item(item["barecode"], item["name"], item["quantity"], item["price"])

    def remove_item(self, barecode):
        """
        Remove an item from the shopping list
        :param str barecode: the item's barecode
        """
        for item in self.items:
            if item["barecode"] == barecode:
                self.items.remove(item)
                break

    def is_valid_barecode(self, barecode):
        """
        Check if the given barecode is valid with a regular expression
        :param str barecode: the item's barecode
        :return: True if the barecode is valid, False otherwise
        """
        return re.match("^[A-Z0-9]{8}$", barecode)