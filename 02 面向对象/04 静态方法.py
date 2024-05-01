class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a


if __name__ == '__main__':
    a = Triangle(3, 4, 5)
    print(Triangle.is_valid(3, 4, 5))
