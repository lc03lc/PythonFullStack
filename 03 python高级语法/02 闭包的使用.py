# 闭包不仅可以保存外部函数的变量，还可以提高代码的复用性

def func_out(name):
    def func_inner(msg):
        info = '{}: {}'.format(name, msg)
        print(info)

    return func_inner


f = func_out("张三")
p = func_out("李四")

f("到北京了吗？")
p("已经到了，放心吧")
f('收到')
p('谢谢！')
