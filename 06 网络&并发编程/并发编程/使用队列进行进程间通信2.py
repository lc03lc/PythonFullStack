import time
from multiprocessing import *


def write(q):
    # 将列表元素写入队列中
    for i in ['a', 'b', 'c']:
        print('开始写入值', i)
        q.put(i)
        time.sleep(1)


def read(q):
    print('开始读取')
    while True:
        if not q.empty():
            print('读取到', q.get())
            time.sleep(1)
        else:
            break


if __name__ == '__main__':
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply(write, (q,))
    pool.apply(read, (q,))
