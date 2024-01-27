import unittest
from prime_numbers_in_range import prime_numbers


class TestPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEqual(prime_numbers(-5, 1), False)
        self.assertEqual(prime_numbers(0, 1), False)
        self.assertEqual(prime_numbers(2, 10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers(100, 110), [101, 103, 107, 109])
