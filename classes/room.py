class Room:
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.guests = []
        self.room_capacity = room_capacity
        self.playlist = []

    def number_of_guests(self):
        return len(self.guests)

    

    def add_guest_to_room(self, guest):
        if len(self.guests) > self.room_capacity:
            return "This room does not have enough space!"
        else:
            self.guests.append(guest)
    
    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)

    def length_of_playlist(self):
        return len(self.playlist)

    def add_song_to_playlist(self, song):
        self.playlist.append(song)