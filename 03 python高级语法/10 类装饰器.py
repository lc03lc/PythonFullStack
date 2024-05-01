# 定义类装饰器
class Check(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        print("登录")
        self.__fn()


@Check
def comment():
    print("发表评论")


comment()
