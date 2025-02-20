# Jean Carlos Farfan Fallu
# 02/23/2025

from superstoreGraph import create_superstore_graph
from gameUtils import (
    print_game_intro,
    print_game_over,
    get_player_answer,
    print_player_routes,
    move_player,
    show_room_item,
    check_player_with_Karen,
    check_player_at_final_room,
    print_Karen_location
)
# Import the node-based stack
from inventoryStack import LinkedStack

def main():
    # Create all rooms and get our start room.
    rooms, start_room = create_superstore_graph()
    current_room = start_room  # "Cafeteria" room
    
    # Stack for player items (capacity 3).
    player_items = LinkedStack(capacity=3)
    
    end_game = False

    # Print intro
    print_game_intro()

    while not end_game:
        # Retrieve current items in a list.
        items_list = player_items.get_items()
        print("Player items:", items_list)

        print_Karen_location(rooms)
        print("Your location:", current_room.name)
        print('---------------------------------------')
        print_player_routes(current_room)
        print('What is your next move? (Type "north", "south", "east", "west", or "exit")')
        direction = get_player_answer()

        # If input is 'exit'.
        if direction == 'Exit':
            end_game = True
            break

        # Move the player.
        current_room = move_player(current_room, direction)

        # Check if Karen is here.
        if check_player_with_Karen(current_room):
            print('You have been caught by the formidable Karen. Your shift is over.')
            break

        # Pick up any item in the room (if user chooses).
        # Now show_room_item expects a stack, so we'll pass player_items.
        show_room_item(current_room, player_items)

        # Check if final room.
        if check_player_at_final_room(current_room):
            # Check if the player has the 3 essential items.
            items_list = player_items.get_items()
            if ('Green vest' in items_list and 
                'Magnetic key' in items_list and 
                'Work phone' in items_list):
                print('You have found all the necessary items and can start working as a slave.')
                print('You win the game.')
                end_game = True
            else:
                print('You do not have the three essential items to finish the game.')

        # Lose if 3 items are in inventory but are not the correct ones.
        # Check if the stack is full and does not have the right combo.
        if player_items.is_full():
            items_list = player_items.get_items()
            has_vest = ('Green vest' in items_list)
            has_key = ('Magnetic key' in items_list)
            has_phone = ('Work phone' in items_list)
            if not (has_vest and has_key and has_phone):
                print("You lose the game because you have the wrong items and do not have enough space in your inventory.")
                end_game = True

    print_game_over()

if __name__ == '__main__':
    main()