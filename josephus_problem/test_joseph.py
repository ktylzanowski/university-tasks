import unittest
from josephus_problem import joseph


class TestPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEqual(joseph(-5, 1), False)
        self.assertEqual(joseph(0, 0), False)
        self.assertEqual(joseph(7, 2), 7)
        self.assertEqual(joseph(5, 3), 4)
