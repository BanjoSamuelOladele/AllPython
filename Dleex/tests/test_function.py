from math import pi
from unittest import TestCase

from functions.functionAndFunction import floating_number
from Week1730th.function import area_of_circle
from Week1730th.function import multiply


class Test(TestCase):
    def test_area_of_circle(self):
        self.assertEquals(area_of_circle(1), pi)

    def test_area_of_circle_again(self):
        self.assertAlmostEquals(area_of_circle(0), 0)

    def test_area_of_circle_returnError_when_a_NegativeValueIs_passed(self):
        self.assertRaises(ValueError, area_of_circle, -2)

    def test_area_of_circle_returnError_when_a_NegativeValueIs_passed_again(self):
        self.assertRaises(TypeError, area_of_circle, "Asa")

    def test_multiply(self):
        self.assertEquals(multiply(2, 2), 4)
        self.assertEquals(multiply(11, 2), 22)

    def test_multiply_again(self):
        self.assertRaises(TypeError, multiply, ("Asa", "Asa"))

    """Using pytest"""

    def test_multiplyAgain(self):
        assert multiply(3, 5) == 15

    def test_float(self):
        self.assertRaises(TypeError, floating_number, (3, 9))
