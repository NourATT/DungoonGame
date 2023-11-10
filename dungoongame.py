from classes import *
import banner
from game_runner import *


player = initialize_player()

print(player)

starter_room = Room("""\nYou are in a dank and musty room of stone bricks and wooden supports, with some barrels and crates scattered about, water dripping from the ceiling. You have a feeling you'll 
see a lot of rooms like this in your immediate future. There are two doorways, the west one with a sign that reads 'TUTORIAL' above it, the north one with a sign that reads 'ADVENTURE.'""")
