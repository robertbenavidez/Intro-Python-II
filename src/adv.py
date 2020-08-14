from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# >>>>>>> Add Items list here >>>>>>>>

item = {
    "sword": Item("Long Sword", "A knight's constant companion"),
    "torch": Item("Torch", "something to light your way"),
    "coins": Item("Gold coins", "50 gold coins"),
}
# >>>>>>> Place items in specific rooms >>>>

room['outside'].add_item(item['torch'].name)

# >>>>>>> Hard code player with name and location >>>>>
player = Player("Robert", room['outside'])


def adv_game():
    print(f'\n  "DUNGEON CRAWLER"\n\n{player.name}, proceed with caution')

    quit = False
    while not quit:
        print(f'{player.current_room}')
        print(player.current_room.items)
        print(f'Inventory: {player.inventory}')

        action = input(f"Choose an action:\n(N)orth\n(S)outh\n(E)ast\n(W)est\n\n(G)rab\n(D)rop\n(Q)uit\n\nCommand:")

        action = action.lower().strip()

        def check_dir(dir):
            if dir:
                player.move(dir)
            else:
                print("\nYou can't move that way! Choose another direction.")

        if len(action.split()) == 1:

            if action == "n":
                check_dir(player.current_room.n_to)

            if action == "s":
                check_dir(player.current_room.s_to)

            if action == "e":
                check_dir(player.current_room.e_to)

            if action == "w":
                check_dir(player.current_room.w_to)

            if action == "q":
                print(f'Thank you for playing DUNGEON CRAWLER')
                exit()
            print(f'action:', action)
        elif (len(action.split())) == 2:
            act = action.split()[0]
            room_item = action.split()[1]

            if act == "grab":
                for item[room_item] in player.current_room.items:
                    player.take_item(item[room_item])
                    player.current_room.remove_item(item[room_item])

            elif act == "drop":
                for item[room_item] in player.inventory:
                    player.drop_item(item[room_item])
                    player.current_room.add_item(item[room_item])


adv_game()
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
