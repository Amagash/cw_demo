import re
class ShoppingList():
    """
    A class  to represent a list  of items to buy.
    """
    def __init__(self):
        """
        Initialise the shopping list.
        """
        self.items = []
    
    def add_item(self, barcode, name, price, quantity):
        """
        Add a new item to the shopping list.
        :param str barcode: The barecode of the item. It is a unique 8 character
        string with only numbers and uppercased letters.
        :param str name: The name of the item.
        :param float price: The price of the item.
        :param int quantity: The quantity of the item.
        :return: None.
        """
        self.items.append({
            "barcode": barcode,
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def add_multiple_items(self, items):
        """
        Add multiple items to the shopping list.
        :param list items: A list of items to add to the shopping list.
        :return: None.
        """
        for item in items:
            self.add_item(item["barcode"], item["name"], item["price"], item["quantity"])

    def remove_item(self, barcode):
        """
        Remove an item from the shopping list.
        :param str barcode: The barecode of the item to remove.
        :return: None.
        """
        self.items = [item for item in self.items if item["barcode"] != barcode]

    def is_valid_barcode(self, barcode):
        """
        Check if the given barcode is valid with a regular expression.
        :param str barcode: The barcode to check.
        :return: True if the barcode is valid, False otherwise.
        """
        return re.match("^[A-Z0-9]{8}$", barcode) is not None