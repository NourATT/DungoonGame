from classes import *

def introscene():
    print(
        """\nYou wake up in a dank and musty room of stone bricks and wooden
        supports. You have no idea how you got here, or what happened after you
        went to bed last night. You remember everything else, except how you like to fight. There are three objects in
front of you - a rusted sword, a moldy-looking bow with a 
quiver and some arrows, and a cracked staff with a gemstone on top.\n""")

def player_choice(prompt, num_choices):
    while True:
        player_input = input(prompt)
        if player_input.isnumeric():
            if int(player_input) in range(1,num_choices+1):
                return int(player_input)
            else:
                print(f"Invalid input, must be a number 1-{num_choices}!")
        else:
            print(f"Invalid input: {player_input} is not a number!")

def fight(weapon,enemy):
    Enemy.health - Weapon.damage
    if Enemy.health > 0:
        Player.health - Enemy.damage