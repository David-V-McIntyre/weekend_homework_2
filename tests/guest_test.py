import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Commander Zavala")

    def test_person_has_name(self):
        self.assertEqual("Commander Zavala", self.guest.name)