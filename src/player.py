class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"Player: {self.name} Current Room: {self.current_room} Player Inventory: {self.inventory}"

    def move(self, room):
        self.current_room = room

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
