"""Using pytest"""
import pytest as pytest

import functions
from Week1730th.function import multiply, subtract
from unittest import TestCase
from Week1730th.function import square
from functions.functionAndFunction import floating_number


def test_float():
    with pytest.raises(TypeError):
        floating_number(7, 8)
        floating_number(6.8, 9)


def test_square():
    assert square(4) == 16


def test_check_state():
    assertTrue: functions.functionAndFunction.check_status(4)


def test_discount():
    assert functions.functionAndFunction.discount(1000, 10) == 900
    assert functions.functionAndFunction.discount(1000, 5) == 950


def test_discount_errors():
    with pytest.raises(TypeError):
        functions.functionAndFunction.discount(0, 10)


def test_discount_errors_again():
    with pytest.raises(TypeError):
        functions.functionAndFunction.discount("0", "o")


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

    def test_floating_function(self):
        self.assertRaises(TypeError, floating_number, (7, 9))

    # def test_float_number(self):
    #     assert TypeError(floating_number(7, 9))
