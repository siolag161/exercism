import unittest

from year import is_leap_year


class YearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertIs(is_leap_year(1996), True)

    def test_non_leap_year(self):
        self.assertIs(is_leap_year(1997), False)

    def test_non_leap_even_year(self):
        self.assertIs(is_leap_year(1998), False)

    def test_century(self):
        self.assertIs(is_leap_year(1900), False)

    def test_century_1(self):
        self.assertIs(is_leap_year(1800), False)

    def test_exceptional_century(self):
        self.assertIs(is_leap_year(2400), True)

    def test_exceptional_century_1(self):
        self.assertIs(is_leap_year(1600), True)

if __name__ == '__main__':
    unittest.main()
