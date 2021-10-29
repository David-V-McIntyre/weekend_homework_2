import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Big Room", 10, 15)
        self.room2 = Room("Little Room", 5, 10)
        self.room3 = Room("Couples Room", 2, 25)

        self.guest1 = Guest("Commander Zavala", 25)
        self.guest2 = Guest("Ikora Rey", 30)
        self.guest3 = Guest("Saint-14", 5000)
        self.guest4 = Guest("Master Chief", 15)

        self.song1 = Song("You! Me! Dancing!", "Los Campesinos!")
        self.song2 = Song("Song 2", "Blur")
        self.song3 = Song("Total Eclipse of the Heart", "Toni Braxton")
        self.song4 = Song("Fresh Prince of Bel Air theme tune", "The Fresh Prince feat. Jazzy Jeff")


    def test_room_has_name(self):
        self.assertEqual("Big Room", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.room3.room_capacity)
    
    
    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, self.room1.number_of_guests())

    def test_remove_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.remove_guest_from_room(self.guest1)
        self.assertEqual(1, self.room1.number_of_guests())

    def test_playlist_starts_empty(self):
        self.assertEqual(0, self.room3.length_of_playlist())

    def test_guests_starts_empty(self):
        self.assertEqual(0, self.room1.number_of_guests())

    def test_add_song_to_playlist(self):
        self.room3.add_song_to_playlist(self.song1)
        self.room3.add_song_to_playlist(self.song2)
        self.assertEqual(2, self.room3.length_of_playlist())
    

    def test_add_guest_to_room_too_small(self):
        self.room3.add_guest_to_room(self.guest1)
        self.room3.add_guest_to_room(self.guest2)
        self.room3.add_guest_to_room(self.guest2)
        self.assertEqual(0, self.room1.number_of_guests())
    
    

    
