import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Commander Zavala")
        self.guest2 = Guest("Ikora Rey")
        self.guest3 = Guest("Saint-14")
        self.guest4 = Guest("Master Chief")

    def test_person_has_name1(self):
        self.assertEqual("Commander Zavala", self.guest1.name)

    def test_person_has_name2(self):
        self.assertEqual("Ikora Rey", self.guest2.name)