import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("You! Me! Dancing!", "Los Campesinos!")
        self.song2 = Song("Song 2", "Blur")
        self.song3 = Song("Total Eclipse of the Heart", "Toni Braxton")
        self.song4 = Song("Fresh Prince of Bel Air theme tune", "The Fresh Prince feat. Jazzy Jeff")

    def test_song_has_title(self):
        self.assertEqual("Song 2", self.song2.title)

    def test_song_has_artist(self):
        self.assertEqual("Toni Braxton", self.song3.artist)