import classes
from helper import player_choice
from rooms import roomstart

def introscene():
    print("""             _                    _         _   _        
 __ __ _____| |__ ___ _ __  ___  | |_ ___  | |_| |_  ___ 
 \ V  V / -_) / _/ _ \ '  \/ -_) |  _/ _ \ |  _| ' \/ -_)
  \_/\_/\___|_\__\___/_|_|_\___| \___\___/ \___|_||_\___|
______  _   _  _   _  _____  _____  _____  _   _ 
|  _  \| | | || \ | ||  __ \|  _  ||  _  || \ | |
| | | || | | ||  \| || |  \/| | | || | | ||  \| |
| | | || | | || . ` || | __ | | | || | | || . ` |
| |/ / | |_| || |\  || |_\ \\\ \_/ /\ \_/ /| |\  |
|___/   \___/ \_| \_/ \____/ \___/  \___/ \_| \_/""")
    print("""\nYou wake up in a dank and musty room of stone bricks and wooden supports. You have no idea how you got here, or what happened after you went to bed last night. You remember
     everything else, except how you like to fight. There are three objects in front of you - a sword, a bow with a 
     quiver and some arrows, and a staff with a gemstone on top.\n""")

    PLAYERCLASS = player_choice("1 = Fighter\n2 = Ranger\n3 = Mage\n\n", 3)
    player = PLAYERCLASS

    if playerdata.PLAYERCLASS == 1:
        print("You nab the sword, and give it some test swings for good measure.")
    elif playerdata.PLAYERCLASS == 2:
        print("You snatch up the bow and strap on the quiver.")
    elif playerdata.PLAYERCLASS == 3:
        print("You grab the staff and immediately feel slightly more wizardy.")
    roomstart()