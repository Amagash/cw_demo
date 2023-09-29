import re
class ShoppingList:
    """
    A class to represent a shopping list of items to buy.
    """
    def __init__(self):
        """
        Constructs en empty shopping list.
        """
        self.items = []
    
    def add_item(self, barcode, name, price, quantity):
        """
        Adds an item to the shopping list.
        :param str barcode: the barcode of the item. The barcode is an 8 character long string
        with only numbers and uppercase letters. 
        :param str name: the name of the item
        :param float price: the price of the item
        :param int quantity: the quantity of the item
        """
        self.items.append(
            {
                "barcode": barcode,
                "name": name,
                "price": price,
                "quantity": quantity
            }
        )

    def add_multiple_items(self, items):
        """
        Adds multiple items to the shopping list.
        :param list items: a list of items to add to the shopping list
        """
        for item in items:
            self.add_item(item["barcode"], item["name"], item["price"], item["quantity"])

    def remove_item(self, barcode):
        """
        Removes an item from the shopping list.
        :param str barcode: the barcode of the item to remove
        """
        for item in self.items:
            if item["barcode"] == barcode:
                self.items.remove(item)
                return
    
    def is_valid_barcode(self, barcode):
        """
        Checks if the given barcode is valid with a regular expression.
        :param str barcode: the barcode to check
        :return: True if the barcode is valid, False otherwise
        """
        return re.match(r"^[A-Z0-9]{8}$", barcode)