import threading

global num
num = 0
lock = threading.Lock()


def fun1():
    global num
    lock.acquire()
    for i in range(1000000):
        num += 1
    lock.release()
    print('fun1', num)


def fun2():
    global num
    lock.acquire()
    for i in range(1000000):
        num += 1
    lock.release()
    print('fun2', num)


if __name__ == '__main__':
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()
