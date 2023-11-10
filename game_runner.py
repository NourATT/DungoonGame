from classes import *
from helper import *
import banner


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
        print("You grab the staff and immediately feel slightly more wizardy.")
    return player


def load_map():
    room_mapping = {}
    for i in range(1, 6):
        room_mapping[i] = Room(i)
    
