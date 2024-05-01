import socket

from config import *


class ServerSocket(socket.socket):
    """初始化服务器套接字需要的相关参数"""

    def __init__(self):
        # 设置为 TCP 类型
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((SERVER_IP, SERVER_PORT))

        # 设置为监听模式
        self.listen(128)
