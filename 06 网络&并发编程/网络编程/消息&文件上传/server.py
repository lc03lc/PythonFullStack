import json
import socket
import struct


def recv_data(conn, chunk_size=1024):
    # 获取头部信息： 固定是4字节 数据长度
    bytes_list = []  # 字节列表
    has_read_size = 0
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        has_read_size += len(chunk)
        bytes_list.append(chunk)
    header = b"".join(bytes_list)
    data_length = struct.unpack("i", header)[0]

    # 获取数据
    data_list = []
    has_read_data_size = 0
    while has_read_data_size < data_length:
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)
        data_list.append(chunk)
        has_read_data_size += len(chunk)
    data = b''.join(data_list)
    return data.decode('utf-8')


def recv_file(conn, chunk_size=1024):
    # 获取头部信息： 固定是4字节 数据长度
    bytes_list = []
    has_read_size = 0
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        has_read_size += len(chunk)
        bytes_list.append(chunk)
    header = b"".join(bytes_list)
    data_length = struct.unpack("i", header)[0]

    # 获取数据
    data_list = []
    has_read_data_size = 0
    while has_read_data_size < data_length:
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)
        data_list.append(chunk)
        has_read_data_size += len(chunk)
    data = b''.join(data_list)
    return data


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()

        while True:
            j = recv_data(conn)
            if j == 'close':
                break
            msg_type = json.loads(j)["msg_type"]

            if msg_type == 'msg':
                msg_content = recv_data(conn)
                print(msg_content)

            else:
                file_data = recv_file(conn)
                file_name = json.loads(j)['file_name']
                object_file = open(file_name, mode='wb')
                object_file.write(file_data)
                print(file_name + " 传输完成！")
        conn.close()

    sock.close()


if __name__ == '__main__':
    run()
