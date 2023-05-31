"""Testing"""
from math import pi


def area_of_circle(radius: int):
    try:
        if radius < 0:
            raise ValueError("no negative valur allowed")
        return pi * (radius ** 2)
    except TypeError:
        raise TypeError("No character allowed")


def multiply(first_number: float, second_number: float):
    return first_number * second_number


def square(number):
    return number ** 2


def subtract(first_number, second_number):
    return first_number - second_number


