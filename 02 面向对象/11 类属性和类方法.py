# 工具类
class Tool:
    # 定义一个类属性
    count = 0
    tool_list = []

    @classmethod
    def PrintCount(cls):
        print(f'工具数量为{cls.count}。')
        print('工具有'+'、'.join(cls.tool_list)+'。')

    def __init__(self, name):
        # 对象属性[实例属性]
        self.name = name
        # 当我们创建对象之后让count + 1
        Tool.count += 1
        Tool.tool_list.append(name)


if __name__ == '__main__':
    tool1 = Tool('斧头')
    # 类属性的获取方式: 类名.类属性
    print(Tool.count)
    tool2 = Tool('锤子')
    print(Tool.count)
    tool3 = Tool('剪刀')
    print(Tool.count)
    # 类方法的调用方式: 类名.类方法
    Tool.PrintCount()
