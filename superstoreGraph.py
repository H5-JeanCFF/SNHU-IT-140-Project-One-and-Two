# Jean Carlos Farfan Fallu
# 02/23/2025

import random
from collections import deque

class Room:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.item = None
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def __str__(self):
        return self.name


# Create and return a Graph of my Wal-Mart store layout.
# Returns a list of rooms and the start room (Cafeteria).
def create_superstore_graph():

     # Create the Room objects
    restroom = Room("Restroom")
    cafeteria = Room("Cafeteria")
    garden = Room("Garden department")
    electronics = Room("Electronics department")
    checkout = Room("Checkout counters")
    entrance = Room("Entrance")
    backroom = Room("Backroom")
    grocery = Room("Grocery department")
    produce = Room("Produce department")
    ogp = Room("Online Grocery Pickup")

    # Link them (N, S, E, W)
    # Restroom
    restroom.south = cafeteria

    # Cafeteria
    cafeteria.north = restroom
    cafeteria.south = garden
    cafeteria.east = electronics

    # Garden
    garden.north = cafeteria
    garden.east = checkout

    # Electronics
    electronics.north = backroom
    electronics.west = cafeteria
    electronics.east = grocery
    electronics.south = checkout

    # Checkout
    checkout.north = electronics
    checkout.east = produce
    checkout.west = garden
    checkout.south = entrance

    # Backroom
    backroom.west = electronics
    backroom.south = grocery
    backroom.east = ogp

    # Grocery
    grocery.north = backroom
    grocery.east = ogp
    grocery.west = electronics
    grocery.south = produce

    # Produce
    produce.north = grocery
    produce.east = ogp
    produce.west = checkout

    # Online Grocery Pickup (OGP)
    ogp.north = backroom
    ogp.south = produce
    ogp.west = grocery

    # Game items
    list_items = ['Green vest', 'Magnetic key', 'Work phone',
                  'Karen', 'Monster energy drink', 'Tacos', 'Great Value bread',
                  'Doge']
    
    # Karen cannot be at the 'Checkout counters' because she might block the
    # path to 'Entrance' room that could contain an essential item needed to
    # win the game.
    while 'Karen' == list_items[3]:
        # Shuffle list of items
        random.shuffle(list_items)

    # Assign random items to some rooms
    restroom.item = list_items[0]
    garden.item = list_items[1]
    electronics.item = list_items[2]
    checkout.item = list_items[3]
    entrance.item = list_items[4]
    backroom.item = list_items[5]
    grocery.item = list_items[6]
    produce.item = list_items[7]

    rooms = [restroom, cafeteria, garden, electronics, checkout,
             entrance, backroom, grocery, produce, ogp]
    
    # return the list of rooms and the initial room (Cafeteria)
    return rooms, cafeteria