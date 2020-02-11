# Circle class
from math import pi


class Circle:
    """
    Be careful with naming convention of setters and getters
    having the samename of setter, getters, attributes will
    raise a RunTimeError: Maximum recursion achieved
    """
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 1:
            raise ValueError('Radius cannot be negative')
        self._radius = radius

    # getter - read only
    @property
    def diameter(self):
        return self.radius * 2

    # setter - read/write
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return self.radius * self.radius * pi

    # string representation
    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'Circle({})'.format(self.radius)
