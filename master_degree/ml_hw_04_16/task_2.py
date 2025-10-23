class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2) ** .5


class Segment3D:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        return self.start_point.distance_to(self.end_point)

    def middle(self):
        x = (self.start_point.x + self.end_point.x) / 2
        y = (self.start_point.y + self.end_point.y) / 2
        z = (self.start_point.z + self.end_point.z) / 2
        return Point3D(x, y, z)


if __name__ == "__main__":
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(2.5, 1, -2)

    s = Segment3D(p1, p2)

    print(s.length())  # 5.315072906367325

    m = s.middle()

    print(type(m) == Point3D)  # True
    print(m.x, m.y, m.z)  # 1.75, 1.5, 0.5
