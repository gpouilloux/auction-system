import uuid

__author__ = "Guillaume Pouilloux <gui.pouilloux@gmail.com>"


# An item has a unique name and reserved price.
# To buy an item, participants must submit bids with
# a price higher than the reserved price.
class Item:
    def __init__(self, name, reserved_price):
        self.id = uuid.uuid1()
        self.name = name
        self.reserved_price = reserved_price
        self.is_sold = False

