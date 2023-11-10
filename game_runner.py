from classes import *
from helper import *
import banner
import json


def initialize_player():
    print(banner.welcome_banner)
    print("""\nYou wake up in a dank and musty room of stone bricks and wooden
supports. You have no idea how you got here, or what happened after you
went to bed last night. You remember everything else, except how you
like to fight. There are three objects in front of you - a sword, a bow
with a quiver and some arrows, and a staff with a gemstone on top.\n""")
    player_class = player_choice("1 = Fighter\n2 = Ranger\n3 = Mage\n\n", 3)
    player = Player(player_class)

    if player.playerclass == 1:
        print("You nab the sword, and give it some test swings for good measure.")
    elif player.playerclass == 2:
        print("You snatch up the bow and strap on the quiver.")
    elif player.playerclass == 3:
        print("You grab the staff and immediately feel slightly more wizardly.")
    return player


def load_map():
    room_file = open("rooms.json", "r")
    room_data = json.load(room_file)
    rooms_as_dicts = room_data["rooms"]
    rooms = {}
    for rad in rooms_as_dicts:
        if "entry_prompt" in rad:
            rooms[rad["id"]] = Room(rad["id"], rad["entry_prompt"])
        else:
            rooms[rad["id"]] = Room(rad["id"])
    for room_id in rooms:
        curr_room = rooms[room_id]
        room_dict = rooms_as_dicts[room_id]
        curr_room.north = room_dict["n"]
        curr_room.south = room_dict["s"]
        curr_room.east = room_dict["e"]
        curr_room.west = room_dict["w"]

    rooms[0] = rooms[room_data["starter"]]
    return rooms


def start_game(player, game_map):
    current_room = game_map[0]
    while player.health > 0:
        print(current_room.entry_prompt)
        
