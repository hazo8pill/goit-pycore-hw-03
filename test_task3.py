import unittest

from task3 import normalize_phone


class TestNormalizePhone(unittest.TestCase):
    def test_examples_from_task(self):
        cases = {
            '067\t123 4567': '+380671234567',
            '(095) 234-5678\n': '+380952345678',
            '+380 44 123 4567': '+380441234567',
            '380501234567': '+380501234567',
            '    +38(050)123-32-34': '+380501233234',
            '     0503451234': '+380503451234',
            '(050)8889900': '+380508889900',
            '38050-111-22-22': '+380501112222',
            '38050 111 22 11   ': '+380501112211',
        }
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(normalize_phone(raw), expected)

    def test_already_normalized_is_unchanged(self):
        self.assertEqual(normalize_phone('+380501234567'), '+380501234567')

    def test_foreign_code_is_kept(self):
        # Has its own '+' code, so '+38' must NOT be added.
        self.assertEqual(normalize_phone('+48 123-456-789'), '+48123456789')

    def test_only_digits_and_leading_plus_remain(self):
        result = normalize_phone(' +38 (050) 123.45.67 ext ')
        self.assertTrue(result.startswith('+'))
        self.assertTrue(result[1:].isdigit(), result)

    def test_returns_str(self):
        self.assertIsInstance(normalize_phone('0501234567'), str)


if __name__ == '__main__':
    unittest.main()
