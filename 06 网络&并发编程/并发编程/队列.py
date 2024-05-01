from multiprocessing import Queue

q = Queue(3)  # 可以指定队列大小，默认为无限

q.put('消息1')
q.put('消息2')
q.put('消息3')

# put方法中参数 队列已经满了，等待1秒，如果还是没有空间，则抛出异常
# q.put('消息4', block=True, timeout=1)

# 判断队列是否已满
if not q.full():
    q.put('消息4', block=True, timeout=1)

# 读取并删除元素 get
print(q.get())
print(q.get())

# 判断是否已空
if not q.empty():
    print(q.get(block=True, timeout=1))

# 查看队列大小
print(q.qsize())