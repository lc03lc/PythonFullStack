# 闭包的构成条件
# 1. 在函数嵌套（函数里面在定义函数）的前提下
# 2. 内部函数使用了外部函数的变量
# 3. 外部函数返回了内部函数

def func_out(num1):
    def func_inner(num2):
        num = num1 + num2
        print('num的值为: ', num)

    return func_inner


f = func_out(10)
f(1)
f(2)
