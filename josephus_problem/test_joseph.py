import unittest
from josephus_problem import joseph


class TestJoseph(unittest.TestCase):
    def test_joseph(self):
        self.assertEqual(joseph(7, 2), 7)
        self.assertEqual(joseph(5, 3), 4)
