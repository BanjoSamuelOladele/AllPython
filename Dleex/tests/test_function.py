from math import pi
from unittest import TestCase

from Week1730th.function import area_of_circle


class Test(TestCase):
    def test_area_of_circle(self):
        self.assertEquals(area_of_circle(1), pi)

    def test_area_of_circle_again(self):
        self.assertAlmostEquals(area_of_circle(0), 0)

    def test_area_of_circle_returnError_when_a_NegativeValueIs_passed(self):
        self.assertRaises(ValueError, area_of_circle, -2)

    def test_area_of_circle_returnError_when_a_NegativeValueIs_passed_again(self):
        self.assertRaises(TypeError, area_of_circle, "Asa")
