import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

conn, addr = sock.accept()

# 接收文件大小
data = conn.recv(1024)
file_total_size = int(data.decode('utf-8'))

# 接收文件内容
file_object = open('xxx.png', mode='wb')
recv_size = 0

while True:
    # 每次最多接收1024字节
    data = conn.recv(1024)
    file_object.write(data)
    file_object.flush()

    recv_size += len(data)
    # 上传完成
    if recv_size == file_total_size:
        break

# 接收完毕，关闭连接
conn.close()
sock.close()
