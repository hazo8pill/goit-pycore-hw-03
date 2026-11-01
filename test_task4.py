import unittest
from datetime import date, timedelta

from task4 import get_upcoming_birthdays

TODAY = date.today()
FMT = '%Y.%m.%d'


def birthday(offset: int) -> str:
    """Birthday string (born in 2000) that falls `offset` days from today."""
    d = TODAY + timedelta(days=offset)
    return d.replace(year=2000).strftime(FMT)  # 2000 is leap, so 29 Feb is safe


def day(offset: int) -> date:
    return TODAY + timedelta(days=offset)


def first_offset(weekday: int) -> int:
    """Offset in 0..6 that lands on the given weekday (Mon=0 ... Sun=6)."""
    return next(o for o in range(7) if day(o).weekday() == weekday)


def congrats(users):
    """Result as {name: congratulation_date} so order doesn't matter."""
    return {u['name']: u['congratulation_date'] for u in get_upcoming_birthdays(users)}


class TestGetUpcomingBirthdays(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_upcoming_birthdays([]), [])

    def test_result_format(self):
        o = first_offset(2)  # Wednesday, never moved
        result = get_upcoming_birthdays([{'name': 'Ann', 'birthday': birthday(o)}])
        self.assertEqual(result, [{'name': 'Ann', 'congratulation_date': day(o).strftime(FMT)}])

    def test_weekday_birthdays_in_window_kept_as_is(self):
        for o in range(7):
            if day(o).weekday() < 5:
                with self.subTest(offset=o, date=day(o)):
                    users = [{'name': 'X', 'birthday': birthday(o)}]
                    self.assertEqual(congrats(users), {'X': day(o).strftime(FMT)})

    def test_saturday_moves_to_monday(self):
        o = first_offset(5)
        users = [{'name': 'Sat', 'birthday': birthday(o)}]
        self.assertEqual(congrats(users), {'Sat': day(o + 2).strftime(FMT)})

    def test_sunday_moves_to_monday(self):
        o = first_offset(6)
        users = [{'name': 'Sun', 'birthday': birthday(o)}]
        self.assertEqual(congrats(users), {'Sun': day(o + 1).strftime(FMT)})

    def test_birthday_already_passed_is_excluded(self):
        users = [{'name': 'Past', 'birthday': birthday(-1)}]
        self.assertEqual(get_upcoming_birthdays(users), [])

    def test_birthday_too_far_is_excluded(self):
        users = [{'name': 'Far', 'birthday': birthday(10)}]
        self.assertEqual(get_upcoming_birthdays(users), [])

    def test_mixed_list_filters_correctly(self):
        o = first_offset(1)  # Tuesday
        users = [
            {'name': 'In', 'birthday': birthday(o)},
            {'name': 'Past', 'birthday': birthday(-3)},
            {'name': 'Far', 'birthday': birthday(30)},
        ]
        self.assertEqual(congrats(users), {'In': day(o).strftime(FMT)})

    def test_does_not_mutate_input(self):
        users = [{'name': 'A', 'birthday': birthday(0)}]
        snapshot = [dict(u) for u in users]
        get_upcoming_birthdays(users)
        self.assertEqual(users, snapshot)


if __name__ == '__main__':
    unittest.main()
