# Jean Carlos Farfan Fallu
# 02/23/2025

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

def print_game_over():
    print("Game Over")
    print("Thank you for playing the game.")

def get_player_answer():
    # Capitalize input to avoid conflicts.
    return input("Answer: ").capitalize()

def print_player_routes(room):
    print('These are your available moves:')
    if room.north: # if 'North' exists in the current room
        print('North (\u2191): {:26}'.format(room.north.name), end='')
    if room.south: # if 'South' exists in the current room
        print('South (\u2193): {:26}'.format(room.south.name), end='')
    if room.east: # if 'East' exists in the current room
        print('East (\u2192): {:26}'.format(room.east.name), end='')
    if room.west: # if 'West' exists in the current room
        print('West (\u2190): {:26}'.format(room.west.name), end='')

    print()

# Attempt to move the player based on direction ('north', 'south', etc.).
# Returns the new room (or the same if invalid).
def move_player(current_room, direction):
    # Capitalize the input (direction)
    direction = direction.capitalize()

    next_room = current_room
    if direction == 'North' and current_room.north:
        next_room = current_room.north
    elif direction == 'South' and current_room.south:
        next_room = current_room.south
    elif direction == 'East' and current_room.east:
        next_room = current_room.east
    elif direction == 'West' and current_room.west:
        next_room = current_room.west
    else:
        print("Oops... Enter the location again. Check if you entered the direction correctly.")

    print()
    return next_room

# If the current_room has an item, prompt user to pick it up or not.
# Returns updated 'player_items' stack.
def show_room_item(current_room, player_items):
    if current_room.item is not None:
        while True:
            print("You can pick " + current_room.item + ". Do you want to pick it up? (Yes/No)")
            answer = get_player_answer()
            if answer == 'Yes':
                # Check if stack is not full, then push
                if not player_items.is_full():
                    success = player_items.push(current_room.item)
                    if success:
                        print("You obtained the " + current_room.item + '.')
                        current_room.item = None
                    else:
                        print("Your inventory is already full! Could not push item.")
                else:
                    print("Your inventory is full!")
                break
            elif answer == 'No':
                break
            else:
                print("You entered the wrong input. Try again.")
    print()
    return player_items

# Checks if the player is located at the Karen room and returns True or False.
def check_player_with_Karen(current_room):
    if current_room.item == 'Karen':
        return True
    else:
        return False

# Checks if the player is located at the final room (OGP) and returns True or False.
def check_player_at_final_room(current_room):  
    if current_room.name == 'Online Grocery Pickup':
        return True
    else:
        return False

def print_Karen_location(rooms):
    karen_location = None
    for r in rooms:
        if r.item == 'Karen':
            karen_location = r.name
            break
    # Print location
    print('Karen location:', karen_location)
