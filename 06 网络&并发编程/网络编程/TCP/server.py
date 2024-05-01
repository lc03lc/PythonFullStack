import socket

# 服务端
# 1. 监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.237.72.168', 8001))  # IP, 端口
sock.listen(5)  # 支持排队等待5人

while True:
    # 2. 等待有人来连接（阻塞）
    conn, addr = sock.accept()  # 等待客户端连接，如果不来会阻塞

    # 3. 等待发送者发送消息（阻塞）
    client_data = conn.recv(1024)  # 等待接收客户端发来的数据
    print(client_data.decode('utf-8'))  # 字节->解码

    # 4.给连接着回复消息
    conn.sendall("hello world".encode('utf-8'))

    # 5. 关闭连接
    conn.close()

# 6. 停止服务端程序
sock.close()
