class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, object):
        print(f'{self.name} is eating {object}.')

    def run(self):
        print(f'{self.name} is running.')


class Dog(Animal):
    def bark(self):
        print(f'{self.name} is barking.')


class XiaoTianDog(Dog):
    def fly(self):
        print(f'XiaoTianDog {self.name} is flying.')


if __name__ == '__main__':
    d = XiaoTianDog('Jack')
    d.fly()
