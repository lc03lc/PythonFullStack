import select
import socket

from config import settings


class SelectServer(object):
    def __init__(self):
        self.host = settings.HOST
        self.port = settings.PORT
        self.socket_object_list = []
        self.conn_handler_map = {}

    def run(self, handler):
        server_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_object.setblocking(False)  # 非阻塞
        server_object.bind((self.host, self.host))
        server_object.listen(5)
        self.socket_object_list.append(server_object)

        while True:
            r, w, e = select.select(self.socket_object_list, [], [], 0.05)
            for sock in r:
                if sock == server_object:
                    print("有新客户端来连接")
                    conn, addr = server_object.accept()
                    self.socket_object_list.append(conn)
                    # 实例化handler类
                    self.conn_handler_map[conn] = handler(conn)
                    continue

                # 新数据到来，执行handler中的__call__方法
                handler_object = self.conn_handler_map[sock]
                result = handler_object.execute()
                if not result:
                    self.socket_object_list.remove(sock)
                    del self.conn_handler_map[sock]
        server_object.close()
