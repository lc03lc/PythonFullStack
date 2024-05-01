# 装饰器作用
# 1. 不修改已有函数的源代码
# 2. 给已有函数增加额外的功能


# 定义一个装饰器
def check(fn):
    def inner():
        print("请先登录")
        fn()

    return inner


# 语法糖，会执行   comment = check(comment)
@check
def comment():
    print("发表评论")


comment()
