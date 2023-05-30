from math import pi
from unittest import TestCase

from Week1730th.function import area_of_circle


class Test(TestCase):
    def test_area_of_circle(self):
        self.assertEquals(area_of_circle(1), pi)

    def test_area_of_circle_again(self):
        self.assertAlmostEquals(area_of_circle(0), 0)
