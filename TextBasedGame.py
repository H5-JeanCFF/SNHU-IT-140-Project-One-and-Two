# Jean Carlos Farfan Fallu
# Project One link: https://snhu-my.sharepoint.com/:w:/g/personal/jean_farfan_snhu_edu/EXJlcoXNTyBCjYtG2Z87LKIBb0eMsFpZmCYEwYlstH6LUA?e=SAeeny

import random


def print_game_over():  # prints game over
    print("Game Over")
    print("Thank you for playing the game.")


def get_player_answer():  # Get player input
    return input('Answer: ').capitalize()


def print_game_intro():  # introduction
    print("Welcome to Wal-mart: the text-based game!")
    print("Instructions:")
    print("- The game is a text-based program where you need to type actions to progress.")
    print("- Players can move from one room to another, deciding whether to go north, south, east, or west.")
    print("- If players enter the wrong direction, the game will show the message: 'You entered the wrong direction. Try again.'")
    print("- Players start the game in the cafeteria.")
    print("- To win the game, the player needs to find three essential items and enter the Online Grocery Pickup (OGP) room.")
    print("- Items are randomly located in rooms throughout the map.")
    print("- The player can only carry a maximum of three items.")
    print("- There are non-essential items scattered throughout the map, so players need to be careful when selecting items.")
    print("- If you pick non-essential items and arrive at the OGP room, you lose the game.")
    print("- Players also lose if they are in the same room as the enemy (Karen).")
    print('- You can only pick three items.\n---------------------------------------')


def get_superstore_map():  # function that creates the map
    # list of items
    list_items = ['Green vest', 'Magnetic key', 'Work phone',
                  'Karen', 'Monster energy drink', 'Tacos', 'Great Value bread',
                  'Doge']
    # Karen cannot be at the 'Checkout counters' because she might block the path to 'Entrance' room that could contain an
    # essential item needed to win the game.
    while 'Karen' == list_items[3]:
        random.shuffle(list_items)
    # Walmart superstore map
    game_map = {'Restroom': {'item': list_items[0], 'South': 'Cafeteria'},
                'Cafeteria': {'North': 'Restroom',
                              'South': 'Garden department',
                              'East': 'Electronics department'},
                'Garden department': {'item': list_items[1], 'North': 'Cafeteria',
                                      'East': 'Checkout counters'},
                'Electronics department': {'item': list_items[2], 'North': 'Backroom',
                                           'South': 'Checkout counters',
                                           'East': 'Grocery department',
                                           'West': 'Cafeteria'},
                'Checkout counters': {'item': list_items[3], 'North': 'Electronics department',
                                      'South': 'Entrance', 'East': 'Produce department',
                                      'West': 'Garden department'},
                'Entrance': {'item': list_items[4], 'North': 'Checkout counters'},
                'Backroom': {'item': list_items[5], 'South': 'Grocery department',
                             'East': 'Online Grocery Pickup',
                             'West': 'Electronics department'},
                'Grocery department': {'item': list_items[6], 'North': 'Backroom',
                                       'South': 'Produce department',
                                       'East': 'Online Grocery Pickup',
                                       'West': 'Electronics department'},
                'Produce department': {'item': list_items[7], 'North': 'Grocery department',
                                       'East': 'Online Grocery Pickup',
                                       'West': 'Checkout counters'},
                'Online Grocery Pickup': {'North': 'Backroom',
                                          'South': 'Produce department',
                                          'West': 'Grocery department'}
                }
    return game_map


def print_player_routes(location, store):  # function that prints the routes the player has available.
    print('These are your available moves:')
    if store[location].get('North'):  # if 'North' exists in the inner dictionary then
        print('North (\u2191): {:26}'.format(store[location]['North']), end='')
    if store[location].get('South'):
        print('South (\u2193): {:26}'.format(store[location]['South']), end='')
    if store[location].get('East'):
        print('East (\u2192): {:26}'.format(store[location]['East']), end='')
    if store[location].get('West'):
        print('West (\u2190): {:26}'.format(store[location]['West']), end='')

    print()


def move_player(location, store, answer):  # function that moves the player to other room
    new_player_location = ''

    if store[location].get(answer):  # if the player input exist in the inner dictionary then
        new_player_location = store[location][answer]  # updating the player location to the new location
    else:
        print("Oops... Enter the location again. Check if you entered the direction correctly.")
        new_player_location = location
    print()
    return new_player_location


def show_room_item(location, store,
                   player_items):  # function that prints the item in the room and asks the player if they want to pick up the item
    answer = ''
    if store[location].get('item'):  # if the room has an item then
        while (answer != "Yes") and (answer != 'No'):  # loop that repeats when the player answer incorrectly
            print('You can pick', store[location]['item'] + '. Do you want to pick it up? (Type "yes" or "no"):')
            answer = get_player_answer()
            if answer == 'Yes':
                if (len(player_items) < 3):
                    player_items.append(store[location]['item'])
                    print("You obtained the " + store[location]['item'] + '.')
                    del store[location]['item']
                else:
                    print("Your inventory is full!")
            elif answer != 'No':
                print("You entered the wrong input. Try again.")
    print()
    return player_items, store


def check_player_with_Karen(location, rooms):  # checks if the player is located at the Karen room and returns True or False
    if rooms[location].get('item') == 'Karen':
        return True
    else:
        return False


def check_player_at_final_room(
        location):  # checks if the player is located at the final room (OGP) and returns True or False
    if location == 'Online Grocery Pickup':
        return True
    else:
        return False


def print_Karen_location(rooms):  # prints Karen (the enemy) location
    Karen_location = ''
    for room, value in rooms.items():
        if value.get('item') == 'Karen':
            Karen_location = room
            break
    print('Karen location: ', Karen_location)


def main():
    # variables
    player_location = 'Cafeteria'
    map_dict = get_superstore_map()
    end_game = False
    player_answer = ''
    player_items = []
    print_game_intro()

    # loop of the game
    while not end_game:
        # print
        print("Player items:", player_items)
        print_Karen_location(map_dict)
        print('---------------------------------------\nYou are in the', player_location, 'room.')
        print_player_routes(player_location, map_dict)
        print('What is your next move? (Type "north", "south", "east", "west", or "exit")')
        player_answer = get_player_answer()

        if player_answer == 'Exit':  # end the game
            end_game = True
            break
        else:
            player_location = move_player(player_location, map_dict,  player_answer)  # move the player to the new location

        if check_player_with_Karen(player_location, map_dict):  # checks if the player is in the enemy room
            print('You have been caught by the formidable Karen. Your shift is over.')
            break
        player_items, map_dict = show_room_item(player_location, map_dict, player_items)

        if check_player_at_final_room(player_location):  # checks if the player is in the final room
            if ((player_items.count('Green vest') == 1) and (player_items.count('Magnetic key') == 1) and
                    (player_items.count('Work phone') == 1)):  # end the game
                print('You have found all the necessary items and can start working as a slave.')
                print('You win the game.')
                end_game = True
            else:
                print('You do not have the three essential items to finish the game.')

        if (((player_items.count('Green vest') != 1) or (player_items.count('Magnetic key') != 1) or
             (player_items.count('Work phone') != 1)) and (len(player_items) == 3)):  # lose the player if he or she does not have the correct items
            print("You lose the game because you have the wrong items and do not have enough space in your inventory.")
            end_game = True
    print_game_over()


if __name__ == '__main__':
    main()
