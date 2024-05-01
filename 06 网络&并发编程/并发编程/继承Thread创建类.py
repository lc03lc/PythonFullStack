import threading
import time


def fun1(interval):
    print('开始运行fun1')
    time.sleep(interval)
    print('运行fun1结束')


def fun2(interval):
    print('开始运行fun2')
    time.sleep(interval)
    print('运行fun2结束')


class MyThread(threading.Thread):
    def __init__(self, func, name, args):
        # 重写父类构造方法，其中func是线程函数，args是传入参数，name是线程名
        super().__init__(target=func, name=name, args=args)

    def run(self):
        self._target(*self._args)


if __name__ == "__main__":
    print('开始运行')
    t1 = MyThread(fun1, 'thread1', (2,))
    t2 = MyThread(fun2, 'thread2', (4,))
    t1.start()
    t2.start()
