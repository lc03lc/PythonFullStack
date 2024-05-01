class Student:
    # python中可以使用__slots__属性限定不可以动态添加属性
    __slots__ = {'name', 'age'}     # 19行报错

    def __init__(self, name, age):
        # 初始化方法中 类的属性
        self.name = name
        self.age = age

    def study(self, subject):
        print(
            "name: " + self.name + ", age: " + self.age + ", is studying " + subject
        )


if __name__ == '__main__':
    s1 = Student('Jack', '19')
    # 动态添加属性
    s1.sex = 'male'
    print(s1.sex)
