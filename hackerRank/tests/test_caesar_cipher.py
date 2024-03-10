from productions.caesar_cipher import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher_lowercase(self):
        result = caesarCipher("abcxyz", 3)
        self.assertEqual(result, "defabc")

    def test_caesar_cipher_uppercase(self):
        result = caesarCipher("ABCXYZ", 3)
        self.assertEqual(result, "DEFABC")

    def test_caesar_cipher_mixed_case(self):
        result = caesarCipher("AbCxyz", 3)
        self.assertEqual(result, "DeFabc")

    def test_caesar_cipher_non_alphabetic(self):
        result = caesarCipher("123!@#", 3)
        self.assertEqual(result, "123!@#")


    def test_caesar_cipher_negative_rotation(self):
        result = caesarCipher("abcxyz", -3)
        self.assertEqual(result, "xyzuvw")

    def test_caesar_cipher_empty_string(self):
        result = caesarCipher("", 5)
        self.assertEqual(result, "")
