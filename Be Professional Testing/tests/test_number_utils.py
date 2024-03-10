from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_17_19_23_is_prime(self):
        prime_list = [17, 19, 23]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        
    def test_give_41_43_47_is_prime(self):
        prime_list = [41, 43, 47]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_8_10_12_is_not_prime(self):
        number_list = [8, 10, 12]
        is_prime = is_prime_list(number_list)
        self.assertFalse(is_prime)

    def test_give_2_3_5_7_11_13_17_19_23_29_is_prime(self):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_31_37_41_43_47_53_is_prime(self):
        prime_list = [31, 37, 41, 43, 47, 53]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_3_6_9_is_not_prime(self):
        number_list = [3, 6, 9]
        is_prime = is_prime_list(number_list)
        self.assertFalse(is_prime)

    def test_give_19_25_31_is_not_prime(self):
        number_list = [19, 25, 31]
        is_prime = is_prime_list(number_list)
        self.assertFalse(is_prime)

    def test_give_empty_list_is_not_prime(self):
        number_list = []
        is_prime = is_prime_list(number_list)
        self.assertFalse(is_prime)
