import time
from multiprocessing import Process


def work1(interval):
    print('1 start')
    time.sleep(interval)
    print('1 end')


def work2(interval):
    print('2 start')
    time.sleep(interval)
    print('2 end')


def work3(interval):
    print('3 start')
    time.sleep(interval)
    print('3 end')


if __name__ == '__main__':
    print('主进程运行')
    p1 = Process(target=work1, args=(3,))
    p2 = Process(target=work2, args=(2,))
    p3 = Process(target=work3, args=(1,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('主进程结束')
