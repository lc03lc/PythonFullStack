class A:
    def test(self):
        print('A--- test方法')

    def demo(self):
        print('A--- demo方法')


class B:
    def test(self):
        print('B--- test方法')

    def demo(self):
        print('B--- demo方法')


# 如果父类出现相同的方法名，那么先继承谁就输出谁
class C(A, B):
    pass


if __name__ == '__main__':
    c = C()
    c.test()
    c.demo()
    # python中提供类的内置方法__mro__查看方法搜索顺序
    print(C.__mro__)
