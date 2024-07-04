# classes have pascal casing(each word with capital first letter) where as functions and variables use all small letters and underscore

class PointKey:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Drawing")

    def point(self):
        print("Poining")


pp = PointKey(10, 20)
print(pp.x)
pp.draw()
pp.x1 = 11
print(pp.x1)


class Person:
    def talk(self):
        print("talk")
        print(f'Hi {self.name}')

    def __init__(self, name):
        self.name = name


sa = Person("saurabh")
sa.talk()
