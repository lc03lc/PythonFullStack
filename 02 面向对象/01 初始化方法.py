class Student:
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
    s1.study('English')
