"""
Композиция — это самая тесная связь "часть-целое", где "части" полностью зависят от "целого" 
и не могут существовать отдельно от него. Если уничтожается "целое", уничтожаются и все его "части".

Пример: Дом и Комнаты. Дом "состоит из" комнат, и если дом разрушится, комнаты перестанут 
существовать, потому что они не могут существовать без дома.
"""

class Room:
    def __init__(self, id):
        self.id = id


class Home:
    def __init__(self, name):
        self.name = name
        self.list_room = []

    def add_room(self, room: Room):
        self.list_room.append(room)


my_home = Home('Мой дом')

my_home.add_room(Room(1))
my_home.add_room(Room(2))
my_home.add_room(Room(2))