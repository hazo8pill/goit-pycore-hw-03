import unittest

from task2 import get_numbers_ticket


class TestGetNumbersTicket(unittest.TestCase):
    def assert_valid_ticket(self, result, lo, hi, quantity):
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), quantity)
        self.assertEqual(len(set(result)), quantity, 'numbers must be unique')
        self.assertEqual(result, sorted(result), 'list must be sorted')
        for n in result:
            self.assertIsInstance(n, int)
            self.assertTrue(lo <= n <= hi, f'{n} out of range {lo}..{hi}')

    def test_example_6_of_49(self):
        self.assert_valid_ticket(get_numbers_ticket(1, 49, 6), 1, 49, 6)

    def test_5_of_36(self):
        self.assert_valid_ticket(get_numbers_ticket(1, 36, 5), 1, 36, 5)

    def test_boundaries_allowed(self):
        self.assert_valid_ticket(get_numbers_ticket(1, 1000, 10), 1, 1000, 10)

    def test_take_whole_range(self):
        self.assertEqual(get_numbers_ticket(1, 10, 10), list(range(1, 11)))

    def test_is_random(self):
        results = {tuple(get_numbers_ticket(1, 1000, 6)) for _ in range(5)}
        self.assertGreater(len(results), 1, 'five calls returned the same ticket')

    def test_invalid_params_return_empty_list(self):
        cases = {
            'min below 1': (0, 49, 6),
            'negative min': (-5, 49, 6),
            'max above 1000': (1, 1001, 6),
            'min greater than max': (49, 1, 6),
            'quantity bigger than range': (1, 5, 6),
            'negative quantity': (1, 49, -1),
        }
        for label, args in cases.items():
            with self.subTest(label, args=args):
                self.assertEqual(get_numbers_ticket(*args), [])


if __name__ == '__main__':
    unittest.main()
