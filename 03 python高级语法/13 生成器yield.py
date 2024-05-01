# 生成器函数调用一次，for循环只执行一次，for循环暂停，下次执行再继续
def gen(n):
    for i in range(n):
        print("开始生成...")
        yield i
        print("生成完成")

g = gen(5)
print(next(g))
print(next(g))