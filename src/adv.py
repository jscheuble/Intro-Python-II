from room import Room
from player import Player
from item import Item

# Declare all the rooms

item = {
    'teeth': Item('Teeth', 'These vampire teeth will suck the robot blood from ur enemies'),
    'fist': Item('Fist', 'This fist of solid gold will knock our ur enemies in 3 punches'),
    'robopup': Item('Robopup', 'Look how cute'),
    'cleats': Item('Cleats', 'To step on ur enemies'),
    'key': Item('Key', 'I wonder what this is for')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['key']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['robopup']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['cleats']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['teeth']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['fist']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

robot_name = input("Welcome to Robot Fight Club. Name your robot:")

# Make a new player object that is currently in the 'outside' room.

active_robot = Player(robot_name, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playing = True

while playing:
    print(f"------{active_robot}------")

    # user input
    next_move = input(
        "Choose a direction: n, e, s, w. press i for inventory, press q to quit \n enter 'take item-name' or 'get item-name' to pickup items \n")

    if len(next_move.split(' ')) == 1:
        # quit game if user inputs q
        if next_move.lower() == 'q':
            print("******Game over******")
            playing = False
        # check for direction and property for selected direction
        elif next_move.lower() == 'n' and active_robot.room.n_to:
            # if property exists, relocate player to new room
            active_robot.room = active_robot.room.n_to
        elif next_move.lower() == 'e' and active_robot.room.e_to:
            active_robot.room = active_robot.room.e_to
        elif next_move.lower() == 's' and active_robot.room.s_to:
            active_robot.room = active_robot.room.s_to
        elif next_move.lower() == 'w' and active_robot.room.w_to:
            active_robot.room = active_robot.room.w_to
        elif next_move.lower() == 'i':
            if active_robot.inventory:
                # print inventory
                for item in active_robot.inventory:
                    print(item)
            else:
                print('Your inventory is empty :(')
        else:
            print("There's nothing over there. Try again \n")
    elif len(next_move.split(' ')) > 1:
        if active_robot.room.items:
            if next_move.startswith('get') or next_move.startswith('take'):
                print(f'Sweet, I got a {active_robot.room.items}')
                active_robot.inventory.append(active_robot.room.items)
                active_robot.room.items = []
