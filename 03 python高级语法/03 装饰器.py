# 装饰器作用
# 1. 不修改已有函数的源代码
# 2. 给已有函数增加额外的功能


def comment():
    print("发表评论")


# 定义一个装饰器
def check(fn):
    def inner():
        print("请先登录")
        fn()

    return inner


# 使用装饰器
comment = check(comment)

comment()
