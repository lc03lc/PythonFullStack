class Student:
    def __init__(self, name, age):
        # 创建私有属性
        # 在python中，属性名前加_是受保护的、加__是私有的
        self.__name = name
        self.__age = age

    def study(self, subject):
        print(
            "name: " + self.__name + ", age: " + self.__age + ", is studying " + subject
        )

    # 通过装饰器来访问或者修改私有属性
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name or None


if __name__ == '__main__':
    s1 = Student('Jack', '18')
    s1.study('English')
    # print(s1.__name)    # 无法访问
    # python中不能严格保证私密性，只是通过更换了变量名导致无法访问。可以通过以下方式进行访问
    print(s1._Student__name)

    s1.name = 'Tom'
    print(s1.name)
