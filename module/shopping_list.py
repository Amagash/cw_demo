import re
class ShoppingList:
    """
    A class used to represent a list of items to buy.
    """
    def __init__(self):
        self.items = []
    
    def add_item(self, barcode, name, price, quantity):
        """
        Adds an item to the list of items to buy.
        :param str barcode: The barcode of the item. A barcode is an 8 character long
        string with only numbers and uppercase letters.
        :param str name: The name of the item.
        :param float price: The price of the item.
        :param int quantity: The quantity of the item.
        :return: None.
        """
        self.items.append({"barcode": barcode, "name": name, "price": price, "quantity": quantity})
    
    def remove_item(self, barcode):
        """
        Removes an item from the list of items to buy in the 
        most efficient way possible without using any 
        other data structures.
        :param str barcode: The barcode of the item.
        :return: None.
        """
        for item in self.items:
            if item["barcode"] == barcode:
                self.items.remove(item)
                break


    def add_multiple_items(self, items):
        """
        Adds multiple items to the list of items to buy.
        :param list items: A list of items to add to the list of items to buy.
        :return: None.
        """
        for item in items:
            self.add_item(item["barcode"], item["name"], item["price"], item["quantity"])

    def is_valid_barcode(self, barcode):
        """
        Checks if the given barcode is valid with a regular expression.
        :param str barcode: The barcode to check.
        :return: True if the barcode is valid, False otherwise.
        """
        return bool(re.match(r"^[A-Z0-9]{8}$", barcode))