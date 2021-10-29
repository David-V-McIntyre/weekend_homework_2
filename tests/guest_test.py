import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Commander Zavala", 25)
        self.guest2 = Guest("Ikora Rey", 30)
        self.guest3 = Guest("Saint-14", 5000)
        self.guest4 = Guest("Master Chief", 15)

        self.room1 = Room("Big Room", 10, 15)
        self.room2 = Room("Little Room", 5, 10)
        self.room3 = Room("Couples Room", 2, 25)

    def test_person_has_name1(self):
        self.assertEqual("Commander Zavala", self.guest1.name)

    def test_person_has_name2(self):
        self.assertEqual("Ikora Rey", self.guest2.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(5000, self.guest3.wallet)
    
        
    def test_customer_pays_entry_fee(self):
        self.guest2.guest_pays_entry_fee(self.room2)
        self.assertEqual(20, self.guest2.wallet)
