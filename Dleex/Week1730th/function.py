"""Testing"""
from math import pi


def area_of_circle(radius: int):
    try:
        if radius < 0:
            raise ValueError("no negative valur allowed")
        return pi * (radius ** 2)
    except TypeError:
        raise TypeError("No character allowed")
