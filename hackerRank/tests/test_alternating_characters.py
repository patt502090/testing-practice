from productions.alternating_characters import alternatingCharacters
import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_alternating_characters_no_deletions(self):
        self.assertEqual(alternatingCharacters('ABABAB'), 0)

    def test_alternating_characters_one_deletion(self):
        self.assertEqual(alternatingCharacters('AAAAA'), 4)

    def test_alternating_characters_empty_string(self):
        self.assertEqual(alternatingCharacters(''), 0)

    def test_alternating_characters_single_character(self):
        self.assertEqual(alternatingCharacters('A'), 0)

    def test_alternating_characters_two_characters(self):
        self.assertEqual(alternatingCharacters('AB'), 0)

    def test_alternating_characters_alternating_ab(self):
        self.assertEqual(alternatingCharacters('ABABABAB'), 0)
