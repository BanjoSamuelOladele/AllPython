"""Using pytest"""
from Week1730th.function import multiply, subtract
from unittest import TestCase
from Week1730th.function import square


class Test(TestCase):
    def test_multiply(self):
        assert multiply(4, 5) == 20
        assert multiply("A", 3) == "AAA"

    def test_square_of_a_number(self):
        assert square(4) == 16

    def test_subtraction(self):
        assert subtract(4, 5) == - 1

    def test_subtraction_again(self):
        assert subtract(10, 5) == 5
