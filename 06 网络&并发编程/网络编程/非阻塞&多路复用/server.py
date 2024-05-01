import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('127.0.0.1', 8080))
server.listen(5)

inputs = [server, ]  # socket对象列表

while True:
    r, w, e = select.select(inputs, [], [], 0.05)
    for sock in r:
        if sock == server:
            conn, addr = sock.accept()
            print("有新连接")
            inputs.append(conn)
        else:
            data = sock.recv(1024)
            if data:
                print("收到新消息: ", data.decode('utf-8'))
                sock.sendall("已收到".encode('utf-8'))
            else:
                print('关闭连接')
                inputs.remove(sock)
