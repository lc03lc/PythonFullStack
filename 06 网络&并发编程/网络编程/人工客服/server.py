import socket

# 1. 监听本机的IP和窗口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

while True:
    # 2. 等待客户端连接，否则阻塞
    conn, addr = sock.accept()
    print('有人来连接了')
    # 3. 连接成功后立即发送
    conn.sendall('欢迎使用xx系统，请输入你想要办理的业务'.encode('utf-8'))

    while True:
        # 4. 等待接收消息
        data = conn.recv(1024)
        if not data:
            break
        data_string = data.decode('utf-8')

        # 5. 回复消息
        conn.sendall('你说啥'.encode('utf-8'))

    print('断开连接了')
    # 5. 关闭与此人的连接
    conn.close()

# 6. 停止服务端程序
sock.close()