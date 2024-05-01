class Student:
    def __init__(self, name, age):
        # 初始化方法中 类的属性
        self.name = name
        self.age = age

    def study(self, subject):
        print(
            "name: " + self.name + ", age: " + self.age + ", is studying " + subject
        )

    # 在python中，有两个下划线包含的方法名，类似“__init__”，成为魔术方法，有特殊用途
    def __repr__(self):
        # 当打印该类不想得到类的类的类型和地址时，而是自定义的内容，用内置的 repr 方法
        return self.name + ": " + self.age


if __name__ == '__main__':
    s1 = Student('Jack', '18')
    print(s1)
