# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.room = room
        self.inventory = inventory

    def __str__(self):
        return 'Robot: {self.name}, Room: {self.room}'.format(self=self)
