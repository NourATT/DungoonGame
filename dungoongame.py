from classes import *
import banner
from game_runner import *


player = initialize_player()
print(player)
game_map = load_map()
start_game(player, game_map)
