class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, object):
        print(f'{self.name} is eating {object}.')

    def run(self):
        print(f'{self.name} is running.')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, object):
        # 方法重写
        print(f'Dog {self.name} is eating {object}.')

    def run(self):
        # 方法拓展
        # super() 是一个对象，指向当前类继承的父类
        super().run()
        # python2.x中这么写，3.x保留但不推荐使用
        # Animal.run(self)
        print(f'This is a dog running.')

    def bark(self):
        print(f'{self.name} is barking.')


if __name__ == '__main__':
    a = Dog('Jack')
    a.run()