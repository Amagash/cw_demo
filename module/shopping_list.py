class ShoppingList:
    """
    A class to represent a list of items to buy. 
    """
    def __init__(self):
        """
        Constructs an empty list for the ShoppingList object.
        """
        self.shopping_list = []

    def add_item(self, name, quantity, price):
        """
        Adds an item to the list. 
        :param str name: The name of the item. 
        :param int quantity: The quantity of the item. 
        :param float price: The price of the item. 
        :return: None. 
        """
        self.shopping_list.append((name, quantity, price))