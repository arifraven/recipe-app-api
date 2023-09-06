"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module """

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 16)
        self.assertEquals(res, 6)
