import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))

while True:
    data, (host, port) = server.recvfrom(1024)   # 阻塞，等待客户端发消息（不是等待连接）
    print(data.decode('utf-8'), host, port)
    server.sendto("好的".encode('utf-8'), (host, port))
