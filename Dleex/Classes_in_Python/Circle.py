import math


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.pi = math.pi

    def area_of_a_class(self):
        return f"{self.pi * self.__radius ** 2}"

    def perimeter_of_a_circle(self):
        return 2 * self.pi * self.__radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("radius below zeo(0) not allowed")

    def __str__(self):
        return f"{self.__radius}"


circle = Circle(2)
print(circle)
a = circle.area_of_a_class()
print(a)
