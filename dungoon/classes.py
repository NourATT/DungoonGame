class Player:
    def __init__(self,playerclass) -> None:
        self.playerclass = playerclass
        if self.playerclass == 1:
            self.health = 100
            self.playermaxhealth = 100
            self.inventory = [Weapon("Rusty Sword","A sword so covered with rust it looks like its prime time was before you were born.",5)]
        elif self.playerclass == 2:
            self.health = 80
            self.playermaxhealth = 80
            self.inventory = [Weapon("Weathered Bow","A bow that looks like it might fall apart in you hands.",12), Item("Arrow","An arrow. What else?", 10)]
        elif self.playerclass == 3:
            self.health = 65
            self.playermaxhealth = 65
            self.inventory = [[Weapon("Splintered Staff","A staff that has a big splinter staright down the middle.",5)]]
        
class Item:
    def __init__(self,name,desc,quan = 1) -> None:
        self.name = name
        self.desc = desc
        self.quan = quan

class Weapon(Item):
    def __init__(self,name,desc,damage) -> None:
        super().__init__(name,desc)
        self.damage = damage

class Goblin:
    def __init__(self) -> None:
        self.health
        self.damage