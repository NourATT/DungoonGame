from helper import player_choice

class Player:
    def __init__(self,player_class) -> None:
        self.player_class = player_class
        if self.player_class == 1:
            self.health = 100
            self.max_health = 100
            self.equipped = [Weapon("Rusty Sword","A sword so covered with rust it looks like its prime time was before you were born.",5)]
        elif self.player_class == 2:
            self.health = 80
            self.max_health = 80
            self.equipped = [Weapon("Weathered Bow","A bow that looks like it might fall apart in you hands.",12), Item("Arrow","An arrow. What else?", 10)]
        elif self.player_class == 3:
            self.health = 65
            self.max_health = 65
            self.equipped = [[Weapon("Splintered Staff","A staff that has a big splinter straight down the middle.",5)]]
            
    def enter_room(room):
        print(room.desc)
        choice = player_choice("1 = Fight\n2 = Search\n3 = Items\n4 = Leave\n\n",4)
        if choice == 1:
            print(wip)



class Item:
    def __init__(self,name,desc,quan = 1) -> None:
        self.name = name
        self.desc = desc
        self.quan = quan

class Weapon(Item):
    def __init__(self,name,desc,damage) -> None:
        super().__init__(name,desc)
        self.damage = damage

class Enemy:
    def __init__(self,name,intro,health,damage_range,aggression,crit_chance) -> None:
        self.intro = intro
        self.name = name
        self.health = health
        self.damage_range = damage_range
        self.aggression = aggression
        self.crit_chance = crit_chance

class Room:
    def __init__(self,searched,treasure,enemies,roomid,desc) -> None:
        self.searched = searched
        self.treasure = treasure
        self.enemies = enemies
        self.roomid = roomid
        self.desc = desc
