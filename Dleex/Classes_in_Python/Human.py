"""Human and it Objects"""
import math


#
#
# class Human:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# # creating an object of class "Human"
# human = Human("Dele")
# print(human)

# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#         self.pi = math.pi
#
#     def area_of_a_class(self):
#         return self.pi * self.radius ** 2
#
#     def perimeter_of_a_circle(self):
#         return 2 * self.pi * self.radius
#
#     def __str__(self):
#         return f"{self.radius}"
#
#
# circle = Circle(4)
# print(circle)

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print("drawing")

    def __str__(self):
        return f'Printing from {self.a} to {self.b}'
    @classmethod
    def point_from_one(cls):
        return 1, 1


point = Point(2, 3)
point.draw()
print(point)
print(point.point_from_one())
