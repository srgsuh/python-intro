import unittest as ut
from dictionary import *

class TestDictionary(ut.TestCase):
    def setUp(self):
        self.words = Dictionary()
        self.word_list = [
            "caMel", "cArAmel", "Cartoon", "cartridge", "CARTOGRAPHY", "carzzzzzzz"
        ]
        self.outer_word = "Python"
        for w in self.word_list:
            self.words.add_word(w)

    def test_get_all_words(self):
        self.assertEqual(self.words.get_all_words(), sorted(self.word_list, key=lambda w: w.casefold()))

    def test_add_word_throws_on_the_same(self):
        self.assertRaises(ValueError, self.words.add_word, self.word_list[0])

    def test_add_word_throws_on_changed_case(self):
        self.assertRaises(ValueError, self.words.add_word, self.word_list[0].lower())
        self.assertRaises(ValueError, self.words.add_word, self.word_list[0].upper())
        self.assertRaises(ValueError, self.words.add_word, self.word_list[0].capitalize())

    def test_add_word_ok(self):
        self.words.add_word(self.outer_word)
        self.assertIn(self.outer_word, self.words.get_all_words())