from helper import player_choice

def roomstart():
    print("""\nYou are in a dank and musty room of stone bricks and wooden supports, with some barrels and crates scattered about, water dripping from the ceiling. You have a feeling you'll 
    see a lot of rooms like this in your immediate future. There are two doorways, the west one with a sign that reads 'TUTORIAL' above it, the north one with a sign that reads 'ADVENTURE.'""")
    nextroom = player_choice("1 = West door\n2 = North door\n\n", 2)
    if nextroom == 1:
        roomtutorial()
    elif nextroom == 2:
        room1c()

def roomtutorial():
    print("""You walk into a notably big room, with training dummies, a couple chests, and a clean atmosphere. There ae also some signs strewn about.""")
    while True:
        choice = player_choice("1 = Actions\n2 = Leave\n\n", 2)
        if choice == 1:
            choice = player_choice("1 = Attack\n2 = Search\n3 = Back\n\n", 3)
            if choice == 1:
                choice = player_choice("1 = Training Dummy 1\n2 = Training Dummy 2\n3 = Training Dummy 3\n4 = Back\n\n", 4)
            if choice == 2:
                choice = player_choice("1 = Check Containers\n2 = Read Signs\n3 = Back\n\n", 3)
            if choice == 3:
                continue
        if choice == 2:
            roomstart()

def room1a():
    print("room 1a")
    nextroom = player_choice("1 = North door\n2 = East door\n\n", 1)
    if nextroom == 1:
        room2a()
    if nextroom == 2:
        room1b()

def room1b():
    print("room 1b")
    nextroom = player_choice("1 = South door\n2 = West door\n3 = East door\n\n", 1)
    if nextroom == 1:
        roomstart()
    if nextroom == 2:
        room1b()
    if nextroom == 3:
        room1d()