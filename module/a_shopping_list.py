import re
class Item:
  def __init__(self, id, name, quantity, price):
    self.id = id
    self.name = name 
    self.quantity = quantity
    self.price = price


  def validate_id(id):
    id_regex = re.compile(r'^[A-Z0-9]{8}$')
    if id_regex.match(id):
      return True
    else:  
      return False
