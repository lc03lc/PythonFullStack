import socket

# 1. 向指定IP发送连接请求
client = socket.socket()
client.connect(('110.42.139.166', 8080))  # 向服务端发起连接（阻塞）

# 2. 连接成功后，发送消息
client.sendall('hello'.encode('utf-8'))

# 3. 等待消息的回复
reply = client.recv(1024)
print(reply.decode('utf-8'))

# 4. 关闭连接
client.close()