from unittest import TestCase
from check import check

class CheckTest(TestCase):

    def test_check(self):
        self.assertEqual(check(10), 10)
        self.assertEqual(check(9), None)


# mut.py --target calculator --unit-test test_calculator -m -c
