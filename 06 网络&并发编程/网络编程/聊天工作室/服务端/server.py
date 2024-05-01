from threading import Thread

import pymysql

from config import *
from response_protocol import ResponseProtocol
from server_socket import ServerSocket
from socket_wrapper import SocketWrapper


class Server(object):
    """服务器核心类"""

    def __init__(self):
        # 创建服务器套接字
        self.server_socket = ServerSocket()
        self.request_handle_function = {
            REQUEST_LOGIN: self.request_login_handle,
            REQUEST_CHAT: self.request_chat_handle
        }
        self.clients = {}
        self.conn = pymysql.connect(host=HOST, port=PORT, user=USER,
                                    password=PASSWORD, charset='utf8', db=DB)

    def startup(self):
        """获取客户端连接，并提供服务"""
        while True:
            # 获取客户端连接
            soc, addr = self.server_socket.accept()
            print("有新客户端连接")
            # 使用套接字生成包装对象
            # 收发消息
            client_soc = SocketWrapper(soc)
            t = Thread(target=self.request_handle, args=(client_soc,))
            t.start()

    def request_handle(self, client_soc):
        """处理客户端请求"""
        while True:
            # 接收客户端数据
            r = client_soc.recv_data()
            if not r:
                # 客户端关闭
                self.remove_offline_user(client_soc)
                client_soc.close()
                break

            # 解析数据
            parse_data = self.parse_request_text(r)
            # print("解析后数据", parse_data)

            # 根据数据调用相应函数
            handle_function = self.request_handle_function.get(parse_data['request_id'])
            if handle_function:
                handle_function(client_soc, parse_data)

    def remove_offline_user(self, client_soc):
        del(self.clients[client_soc])

    def parse_request_text(self, r):
        """
        登录信息: 0001|username|password
        聊天信息: 0002|username|messages
        """
        request_list = r.split(DELIMITER)
        # 按照类型解析数据
        request_data = {}
        request_data['request_id'] = request_list[0]

        if request_data['request_id'] == REQUEST_LOGIN:
            request_data['username'] = request_list[1]
            request_data['password'] = request_list[2]

        elif request_data['request_id'] == REQUEST_CHAT:
            request_data['username'] = request_list[1]
            request_data['messages'] = request_list[2]

        return request_data

    def request_login_handle(self, client_sock, request_data):
        """处理用户登录"""
        # 登录用户名和密码
        username = request_data['username']
        password = request_data['password']

        # 查询用户名是否合法
        ret, nickname, username = self.check_user_login(username, password)

        # 如果登录成功，保存连接套接字
        if ret == '1':
            self.clients[username] = {'sock': client_sock, 'nickname': nickname}

        # 组装响应结果
        response_text = ResponseProtocol.response_login(ret, nickname, username)

        # 发送响应结果
        client_sock.send_data(response_text)

    def request_chat_handle(self, client_sock, request_data):
        """处理聊天请求"""
        # 登录用户名和聊天消息
        username = request_data['username']
        messages = request_data['messages']
        nickname = self.clients[username]['nickname']

        # 拼接发送给客户端的消息文本
        msg = ResponseProtocol.response_chat(nickname, messages)

        # 转发给其他用户
        for u_name, info, in self.clients.items():
            if username == u_name:
                continue
            info['sock'].send_data(msg)

    def check_user_login(self, username, password):
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute("select * from " + TB + " where name = %s and password = %s", [username, password])
        result = cursor.fetchone()

        if result:
            cursor.execute("select nickname from " + TB + " where name = '{}'".format(username))
            nickname = cursor.fetchone()
            return '1', *nickname, username

        else:
            return '0', '', ''

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    Server().startup()
