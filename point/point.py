class Point:
    # Attributes
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # String representation
    def __str__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    # Comparison between objects
    def __eq__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return (x1, y1, z1) == (x2, y2, z2)

    # Bonus 1
    # Allow objects to be added and substracted
    def __add__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other

        return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other

        return Point(x1 - x2, y1 - y2, z1 - z2)

    # Bonus 2
    # Allow objects to be scaled up and down by numbers
    def __mul__(self, scalar):
        # obj * int
        x, y, z = self
        return Point(x * scalar, y * scalar, z * scalar)

    def __rmul__(self, scalar):
        # int * obj
        return self.__mul__(scalar)

    # Bonus 3
    # Allow point objects to be unpacked
    def __iter__(self):
        yield from (self.x, self.y, self.z)
