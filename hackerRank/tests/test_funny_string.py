from productions.funny_string import funnyString
import unittest

class TestFunnyString(unittest.TestCase):
    def test_funny_string_positive(self):
        self.assertEqual(funnyString('acxz'), 'Funny')

    def test_funny_string_negative(self):
        self.assertEqual(funnyString('bcxz'), 'Not Funny')

    def test_funny_string_empty(self):
        self.assertEqual(funnyString(''), 'Funny')

    def test_funny_string_single_character(self):
        self.assertEqual(funnyString('a'), 'Funny')

    def test_funny_string_repeating_characters(self):
        self.assertEqual(funnyString('aaa'), 'Funny')

    def test_funny_string_mixed_characters(self):
        self.assertEqual(funnyString('abcde'), 'Funny')
