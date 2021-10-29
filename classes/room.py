class Room:
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.guests = []
        self.room_capacity = room_capacity
        self.song_in_room = []

    def number_of_guests(self):
        return len(self.guests)

    def add_guest_to_room(self, guest):
        self.guests.append(guest)
    
    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)