import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.Room1 = Room("Big Room", 10)
        self.Room2 = Room("Little Room", 5)
        self.Room3 = Room("Couples Room", 2)

        self.guest1 = Guest("Commander Zavala")
        self.guest2 = Guest("Ikora Rey")
        self.guest3 = Guest("Saint-14")
        self.guest4 = Guest("Master Chief")

    def test_room_has_name(self):
        self.assertEqual("Big Room", self.Room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.Room3.room_capacity)
    
    
    def test_add_guest_to_room(self):
        self.Room1.add_guest_to_room(self.guest1)
        self.Room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, self.Room1.number_of_guests())