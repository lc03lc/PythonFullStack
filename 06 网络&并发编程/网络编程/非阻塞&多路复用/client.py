import select
import socket

client_list = []

for i in range(5):
    client = socket.socket()
    client.setblocking(False)

    try:
        # 连接服务器，虽然有异常BlockingIOError，但还是正常发送连接请求
        client.connect(('127.0.0.1', 8080))
    except BlockingIOError as e:
        pass

    client_list.append(client)

recv_list = []  # 放入已连接成功且已经发送数据的socket
while True:
    r, w, e = select.select(recv_list, client_list, [], 0.1)
    for sock in w:
        sock.sendall('你好'.encode('utf-8'))
        recv_list.append(sock)
        client_list.remove(sock)

    for sock in r:
        data = sock.recv(1024)
        print(data.decode('utf-8'))

    if not recv_list and not client_list:
        break
