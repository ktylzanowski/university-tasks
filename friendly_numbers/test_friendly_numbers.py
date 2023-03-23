import unittest
from friendly_numbers import divSum


class TestFriendly(unittest.TestCase):
    def test_friendly_numbers(self):
        self.assertEqual(divSum(-100, 100), {})
        self.assertEqual(divSum(0, 200000), {220: 284, 1184: 1210, 2620: 2924, 5020: 5564, 6232: 6368, 10744: 10856,
                                             12285: 14595, 17296: 18416, 63020: 76084, 66928: 66992, 67095: 71145,
                                             69615: 87633, 79750: 88730, 100485: 124155, 122265: 139815, 122368: 123152,
                                             141664: 153176, 142310: 168730, 171856: 176336, 176272: 180848})
