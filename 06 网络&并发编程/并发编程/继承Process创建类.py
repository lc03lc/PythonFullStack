import time
from multiprocessing import Process


class ClockProcess(Process):  # 继承Process类
    def __init__(self, interval):
        super().__init__()  # 重写初始化
        self.interval = interval

    def run(self):  # 重写run方法，调用start()时就是调用run()
        print('子进程开始执行时间：{}'.format(time.ctime()))
        time.sleep(self.interval)
        print('子进程结束时间：{}'.format(time.ctime()))


if __name__ == '__main__':
    p = ClockProcess(2)
    print('主程序开始运行')
    p.start()
    p.join()
    print('主程序结束运行')
