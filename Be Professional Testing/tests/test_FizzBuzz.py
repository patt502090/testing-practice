from coe_FizzBuzz.FizzBuzz import FizzBuzz
import unittest
class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_divisible_by_3_and_5(self):
        self.assertEqual(FizzBuzz(15), 'FizzBuzz')

    def test_fizzbuzz_divisible_by_3(self):
        self.assertEqual(FizzBuzz(9), 'Fizz')

    def test_fizzbuzz_divisible_by_5(self):
        self.assertEqual(FizzBuzz(25), 'Buzz')

    def test_fizzbuzz_negative_number(self):
        self.assertEqual(FizzBuzz(-15), 'FizzBuzz')

    def test_fizzbuzz_zero(self):
        self.assertEqual(FizzBuzz(0), 'FizzBuzz')