import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.Room1 = Room("Big Room", 10)
        self.Room2 = Room("Little Room", 5)
        self.Room3 = Room("Couples Room", 2)

        self.guest1 = Guest("Commander Zavala")
        self.guest2 = Guest("Ikora Rey")
        self.guest3 = Guest("Saint-14")
        self.guest4 = Guest("Master Chief")

        self.song1 = Song("You! Me! Dancing!", "Los Campesinos!")
        self.song2 = Song("Song 2", "Blur")
        self.song3 = Song("Total Eclipse of the Heart", "Toni Braxton")
        self.song4 = Song("Fresh Prince of Bel Air theme tune", "The Fresh Prince feat. Jazzy Jeff")


    def test_room_has_name(self):
        self.assertEqual("Big Room", self.Room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.Room3.room_capacity)
    
    
    def test_add_guest_to_room(self):
        self.Room1.add_guest_to_room(self.guest1)
        self.Room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, self.Room1.number_of_guests())

    def test_remove_guest_to_room(self):
        self.Room1.add_guest_to_room(self.guest1)
        self.Room1.add_guest_to_room(self.guest2)
        self.Room1.remove_guest_from_room(self.guest1)
        self.assertEqual(1, self.Room1.number_of_guests())

    def test_playlist_starts_empty(self):
        self.assertEqual(0, self.Room3.length_of_playlist())

    def test_guests_starts_empty(self):
        self.assertEqual(0, self.Room1.number_of_guests())

    def test_add_song_to_playlist(self):
        self.Room3.add_song_to_playlist(self.song1)
        self.Room3.add_song_to_playlist(self.song2)
        self.assertEqual(2, self.Room3.length_of_playlist())
    

    def test_add_guest_to_room_too_small(self):
        self.Room3.add_guest_to_room(self.guest1)
        self.Room3.add_guest_to_room(self.guest2)
        self.Room3.add_guest_to_room(self.guest2)
        self.assertEqual(0, self.Room1.number_of_guests())

    
