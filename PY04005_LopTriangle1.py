from math import *

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        d1 = self.p1.distance(self.p2)
        d2 = self.p2.distance(self.p3)
        d3 = self.p3.distance(self.p1)
        if max(d1, d2, d3) * 2 >= d1 + d2 + d3:
            print('INVALID')
        else:
            print(f'{round(d1 + d2 + d3,3):.3f}')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(float, input().split()))
        p1 = Point(arr[0], arr[1])
        p2 = Point(arr[2], arr[3])
        p3 = Point(arr[4], arr[5])
        triangle = Triangle(p1, p2, p3)
        triangle.perimeter()