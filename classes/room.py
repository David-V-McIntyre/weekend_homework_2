class Room:
    def __init__(self, room_name, room_capacity, entry_fee):
        self.room_name = room_name
        self.guests = []
        self.room_capacity = room_capacity
        self.playlist = []
        self.entry_fee = entry_fee

    def number_of_guests(self):
        return len(self.guests)

    def add_guest_to_room(self, guest):
        self.guests.append(guest)
        if self.number_of_guests() > self.room_capacity:
            self.guests.clear()
            return "room is too small"
        
        
    
    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)

    def length_of_playlist(self):
        return len(self.playlist)

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
    

  
