from classes import *
from helper import *
from titlescreen import *

titlescreen()

player_class = player_choice("1 = Fighter\n2 = Ranger\n3 = Mage\n\n", 3)
player = Player(player_class)

if player_class == 1:
    print("You nab the sword, and give it some test swings for good measure.")
elif player_class == 2:
    print("You snatch up the bow and strap on the quiver.")
elif player_class == 3:
    print("You grab the staff and immediately feel slightly more wizardy.")
