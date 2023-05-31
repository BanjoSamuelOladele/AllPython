"""Using pytest"""
import pytest as pytest

import functions
from Week1730th.function import multiply, subtract
from unittest import TestCase
from Week1730th.function import square
from functions.functionAndFunction import floating_number
from functions.List_ import list_to_zero


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


def test_discount_errors_ValueError():
    with pytest.raises(ValueError):
        functions.functionAndFunction.discount(0, 10)


def test_discount_errors_():
    with pytest.raises(ValueError):
        functions.functionAndFunction.discount(3, 7)


def test_discount_errors_again():
    with pytest.raises(TypeError):
        functions.functionAndFunction.discount("3", "7")


def test_list_element_to_zero():
    lst = [1, 2, 3, 4, 5, 6, 7]
    assert list_to_zero(lst) == [0, 2, 3, 4, 5, 6, 0]
    lst1 = [3, 4, 5, 67, 45, 32, 1]
    assert list_to_zero(lst1) == [0, 4, 5, 67, 45, 32, 0]


def test_list_element_with_another_data_structure():
    with pytest.raises(TypeError):
        list_to_zero(3)


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
