import json
import os
import socket
import struct


def send_data(conn, content):
    data = content.encode('utf-8')
    header = struct.pack('i', len(data))
    conn.sendall(header)
    conn.sendall(data)


def send_file(conn, file_path):
    file_size = os.stat(file_path).st_size
    header = struct.pack('i', file_size)
    conn.sendall(header)

    has_send_size = 0
    file_object = open(file_path, mode='rb')
    while has_send_size < file_size:
        chunk = file_object.read(2048)
        conn.sendall(chunk)
        has_send_size += len(chunk)
    file_object.close()


def run():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    while True:
        '''
        消息格式：
            -消息：msg|你好吖
            -文件：file|xxx.png
        '''
        content = input(">>>")
        if content.upper() == "Q":
            send_data(client, "close")
            break
        input_text_list = content.split('|')
        if len(input_text_list) != 2:
            print("格式错误，请重新输入")
            continue
        message_type, info = input_text_list

        # 发消息
        if message_type == 'msg':
            # 发消息类型
            send_data(client, json.dumps({"msg_type": "msg"}))
            # 发内容
            send_data(client, info)

        # 发文件
        else:
            # 文件名
            file_name = info.rsplit(os.sep, maxsplit=1)[-1]
            # 发消息类型
            send_data(client, json.dumps({"msg_type": "file", "file_name": file_name}))
            # 发内容
            send_file(client, info)
    client.close()


if __name__ == '__main__':
    run()
