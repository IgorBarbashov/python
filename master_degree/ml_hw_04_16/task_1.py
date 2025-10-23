class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2) ** .5


if __name__ == "__main__":
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(2.5, 1, -2)

    print(p1.distance_to(p2))
