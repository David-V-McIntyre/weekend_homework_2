class Room:
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.guests = []
        self.room_capacity = room_capacity
        self.song_in_room = []