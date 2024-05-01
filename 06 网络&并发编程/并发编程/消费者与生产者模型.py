import queue  # 多线程模块和队列模块
import threading

que = queue.Queue()  # 创建队列


# 建立消费者模型类
class Consumer(threading.Thread):  # 继承线程列使用

    def __init__(self, que):  # 参数传入队列对象
        super(Consumer, self).__init__()  # 继承祖宗类的初始化方法使用
        self.que = que  # 自定义队列对象属性
        self.start()  # 自动启动线程

    def run(self):  # 线程自带的方法，运行时会自动调用
        # 消费者逻辑，不考虑生产者，只需要从队列里面不断获取任务
        while True:
            # 获取队列任务
            item = self.que.get()
            print(f"消费者消费了{item}")


# 建立生产者模型类
class Producer(threading.Thread):

    def __init__(self, que):  # 参数传入队列对象
        super(Producer, self).__init__()  # 继承祖宗类的初始化方法使用
        self.que = que  # 自定义队列对象属性
        self.start()

    def run(self):  # run方法线程自带的方法 运行时会自动调用
        # 生产者逻辑，不考虑消费者，只需要不断生产任务
        import random, time
        while True:
            time.sleep(1)
            item = random.randint(1, 100)
            print(f"生产了{item}")
            # 生产任务
            self.que.put(item)


# 实例化线程对象
con = Consumer(que)
pro = Producer(que)
