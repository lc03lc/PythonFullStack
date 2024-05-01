class SocketWrapper(object):
    """套接字包装类"""

    def __init__(self, sock):
        self.sock = sock

    def recv_data(self):
        return self.sock.recv(512).decode('utf-8')

    def send_data(self, msg):
        self.sock.send(msg.encode('utf-8'))
