"""Using pytest"""
from Week1730th.function import multiply
from unittest import TestCase
from  Week1730th.function import square


class Test(TestCase):
    def test_multiply(self):
        assert multiply(4, 5) == 20
        assert multiply("A", 3) == "AAA"

    def test_square_of_a_number(self):
        assert square(4) == 16
