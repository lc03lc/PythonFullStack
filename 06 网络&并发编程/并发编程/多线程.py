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


if __name__ == '__main__':
    print('开始运行')
    # 启动多线程
    t1 = threading.Thread(target=fun1, args=(3,))
    t2 = threading.Thread(target=fun2, args=(3,))
    t1.start()
    t2.start()