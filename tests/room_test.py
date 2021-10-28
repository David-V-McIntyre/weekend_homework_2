import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.Room1 = Room("Big Room", 10)
        self.Room2 = Room("Little Room", 5)
        self.Room3 = Room("Couples Room", 2)

    def test_room_has_name(self):
        self.assertEqual("Big Room", self.Room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.Room3.room_capacity)