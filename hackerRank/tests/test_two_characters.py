from productions.two_characters import alternate
import unittest
class TwoCharactersTest(unittest.TestCase):
    def test_alternate_example(self):
        result = alternate("beabeefeab")
        self.assertEqual(result, 5)

    def test_alternate_empty_string(self):
        result = alternate("")
        self.assertEqual(result, 0)

    def test_alternate_single_char(self):
        result = alternate("a")
        self.assertEqual(result, 0)

    def test_alternate_all_same_char(self):
        result = alternate("aaaaa")
        self.assertEqual(result, 0)

    def test_alternate_two_different_chars(self):
        result = alternate("ababab")
        self.assertEqual(result, 6)
        





