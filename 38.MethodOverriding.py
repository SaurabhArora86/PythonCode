class Area:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Area):
    def __init__(self, r):
        super().__init__(r, r)

    def area(self):
        return 3.14 * super().area()


rec = Area(10, 2)
print(rec.area())

cir = Circle(5)
print(cir.area())


class Parallelogrm(Area):
    def __init__(self, l):
        super().__init__(l, l)

    def area(self):
        return super().area()


p1 = Parallelogrm(10)
print(p1.area())
