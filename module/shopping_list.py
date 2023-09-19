import re
class ShoppingList:
    """
    Class to represent a list of items to buy
    """
    def __init__(self):
        """
        Constructs an empty shopping list.
        """
        self.items = []
    
    def add_item(self, barcode, name, price, quantity):
        """
        Adds an item to the shopping list.
        :param str barcode: The barcode of the item. The barcode is a unique 
        8 character string with only numbers and uppercase letters.
        :param str name: The name of the item
        :param float price: The price of the item
        :param int quantity: The quantity of the item
        """
        self.items.append({
            "barcode": barcode,
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def add_multiple_items(self, items):
        """
        Adds multiple items to the shopping list.
        :param list items: A list of items to add to the shopping list.
        """
        for item in items:
            self.add_item(item["barcode"], item["name"], item["price"], item["quantity"])

    def remove_item(self, barcode):
        """
        Removes an item from the shopping list.
        :param str barcode: The barcode of the item to remove.
        """
        for item in self.items:
            if item["barcode"] == barcode:
                self.items.remove(item)
                break

    def is_valid_barcode(self, barcode):
        """
        Checks if a barcode is valid with a regular expression.
        :param str barcode: The barcode to check.
        :return: True if the barcode is valid, False otherwise.
        """
        return bool(re.match("^[A-Z0-9]{8}$", barcode))
