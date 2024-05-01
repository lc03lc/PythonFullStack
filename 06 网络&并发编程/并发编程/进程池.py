import time
from multiprocessing import Pool


def func(msg):
    print('start: ', msg)
    time.sleep(3)
    print('end: ', msg)


if __name__ == '__main__':
    p = Pool(processes=3)
    for i in range(5):
        msg = 'hello{}'.format(i)
        p.apply_async(func, (msg,))
    p.close()
    p.join()
