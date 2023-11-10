class Room:
    def __init__(self, room_id, entry_prompt="You are in a room. What do you do?"):
        self.room_id = room_id
        self.entry_prompt = entry_prompt


class Player:
    def __init__(self, playerclass) -> None:
        self.playerclass = playerclass
        if self.playerclass == 1:
            self.health = 100
            self.playermaxhealth = 100
            self.inventory = [
                Weapon(
                    "Rusty Sword",
                    "A sword so covered with rust it looks like its prime time was before you were born.",
                    5)]
        elif self.playerclass == 2:
            self.health = 80
            self.playermaxhealth = 80
            self.inventory = [
                Weapon(
                    "Weathered Bow",
                    "A bow that looks like it might fall apart in you hands.", 12),
                Item("Arrow", "An arrow. What else?", 10)]
        elif self.playerclass == 3:
            self.health = 65
            self.playermaxhealth = 65
            self.inventory = [
                Weapon(
                    "Splintered Staff",
                    "A staff that has a big splinter straight down the middle.",
                    5)]
        self.equipped_weapon = self.inventory[0]

    def __str__(self) -> str:
        return f"\nHealth: {self.health}/{self.playermaxhealth}\nWeapon: {self.equipped_weapon.name}\nDamage: {self.equipped_weapon.damage}\n"

    def enter_room(self, room: Room) -> None:
        print(room.entry_prompt)


class Item:
    def __init__(self, name, desc, quan=1) -> None:
        self.name = name
        self.desc = desc
        self.quan = quan


class Weapon(Item):
    def __init__(self, name, desc, damage) -> None:
        super().__init__(name, desc)
        self.damage = damage


class Goblin:
    def __init__(self) -> None:
        self.health = 100
        self.damage = 100
