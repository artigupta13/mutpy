from unittest import TestCase
from calculator import mul

class CalculatorTest(TestCase):

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)


# mut.py --target calculator --unit-test test_calculator -m -c        
