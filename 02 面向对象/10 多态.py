class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        dog.game()
        print('%s and %s are playing together.' % (self.name, dog.name))


class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f'{self.name} is playing.')


class XiaoTianDog(Dog):
    def game(self):
        super().game()
        print('This is XiaoTianDog playing.')


if __name__ == '__main__':
    p = Person('Jack')
    d = XiaoTianDog('Xtg')
    p.game_with_dog(d)
