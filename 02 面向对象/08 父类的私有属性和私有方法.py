class A:
    def __init__(self):
        # 创建共有属性
        self.num_1 = 100
        # 创建私有属性
        self.__num_2 = 200

    def __task(self):
        print(f'私有属性和共有属性分别是{self.__num_2}, {self.num_1}')


class B(A):
    def demo(self):
        # 无法访问父类的私有方法, 24行报错
        super().__task()


if __name__ == '__main__':
    b = B()
    print(b.num_1)
    # 无法访问父类的私有属性
    # print(b.__num_2)

    # b.demo()
