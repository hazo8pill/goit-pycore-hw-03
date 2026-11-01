import unittest
from datetime import date, timedelta

from task1 import DateFormatError, get_days_from_today


def iso(days_ago: int) -> str:
    """Date string `days_ago` days before today (negative = future)."""
    return (date.today() - timedelta(days=days_ago)).strftime('%Y-%m-%d')


class TestGetDaysFromToday(unittest.TestCase):
    def test_today_is_zero(self):
        self.assertEqual(get_days_from_today(iso(0)), 0)

    def test_past_is_positive(self):
        self.assertEqual(get_days_from_today(iso(1)), 1)
        self.assertEqual(get_days_from_today(iso(365)), 365)

    def test_future_is_negative(self):
        self.assertEqual(get_days_from_today(iso(-1)), -1)
        self.assertEqual(get_days_from_today(iso(-157)), -157)

    def test_far_dates(self):
        self.assertEqual(get_days_from_today(iso(10_000)), 10_000)
        self.assertEqual(get_days_from_today(iso(-10_000)), -10_000)

    def test_returns_int(self):
        self.assertIs(type(get_days_from_today(iso(5))), int)

    def test_fixed_date_matches_manual_math(self):
        expected = (date.today() - date(2020, 10, 9)).days
        self.assertEqual(get_days_from_today('2020-10-09'), expected)

    def test_leap_day(self):
        expected = (date.today() - date(2024, 2, 29)).days
        self.assertEqual(get_days_from_today('2024-02-29'), expected)

    def test_bad_input_raises_date_format_error(self):
        bad_inputs = [
            '09.10.2020',   # wrong format
            '2020/10/09',   # wrong separator
            '2020-13-01',   # month out of range
            '2023-02-29',   # not a leap year
            'hello',
            '',
            None,
            20201009,
        ]
        for value in bad_inputs:
            with self.subTest(value=value):
                with self.assertRaises(DateFormatError):
                    get_days_from_today(value)


if __name__ == '__main__':
    unittest.main()
