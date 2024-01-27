import unittest
from date_sorting import date_into_dict


class TestDate(unittest.TestCase):
    def test_date(self):
        self.assertEqual(date_into_dict(["24/3/2023", "11/4/2022", "6/7/1999"]), {0: {'day': 6, 'month': 7, 'year': 1999},
                1: {'day': 11, 'month': 4, 'year': 2022}, 2: {'day': 24, 'month': 3, 'year': 2023}})
        self.assertEqual(date_into_dict(["15/3/2021", "14/8/2022", "4/9/2004"]), {0: {'day': 4, 'month': 9, 'year': 2004},
                1: {'day': 15, 'month': 3, 'year': 2021}, 2: {'day': 14, 'month': 8, 'year': 2022}})