class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color_value = color

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def color(self):
        return self.color_value.title()

if __name__ == '__main__':
    arr = input().split()
    width = int(arr[0])
    height = int(arr[1])
    color = arr[2]
    if width <= 0 or height <= 0:
        print("INVALID")
    else:
        r = Rectangle(width, height, color)
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))