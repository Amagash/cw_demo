class ShoppingList:
    """
    A class to represent a list of items to buy. 
    """
    def __init__(self):
        """
        Constructs an empty list for the ShoppingList object.
        """
        self.items = []

    def add_item(self, name, quantity, price):
        """
        Adds an item to the list. 
        :param str name: The name of the item. 
        :param int quantity: The quantity of the item. 
        :param float price: The price of the item. 
        :return: None. 
        """
        self.items.append(
            {
                "name": name,
                "quantity": quantity,
                "price": price
            }
        )
    
    def remove_item(self, name):
        """
        Removes an item from the list. 
        :param str name: The name of the item. 
        :return: None. 
        """
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                break

    def add_multiple_items(self, list_of_items):
        """
        Adds multiple items to the list. 
        :param list list_of_items: A list of items. 
        :return: None. 
        """
        for item in list_of_items:
            self.add_item(item["name"], item["quantity"], item["price"])