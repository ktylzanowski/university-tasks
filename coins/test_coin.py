import unittest

from coin_change_problem import num_coins


class TestNumCoins(unittest.TestCase):
    def test_empty_coins(self):
        coins = []
        amount = 10
        self.assertEqual(num_coins(coins, amount), 0)

    def test_zero_amount(self):
        coins = [1, 2, 5]
        amount = 0
        self.assertEqual(num_coins(coins, amount), 0)

    def test_no_solution(self):
        coins = [2, 4, 6]
        amount = 11
        self.assertEqual(num_coins(coins, amount), -1)

    def test_single_coin(self):
        coins = [1]
        amount = 10
        self.assertEqual(num_coins(coins, amount), 10)

    def test_small_case(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(num_coins(coins, amount), 3)

    def test_large_case(self):
        coins = [1, 5, 10, 25, 50]
        amount = 234
        self.assertEqual(num_coins(coins, amount), 9)
