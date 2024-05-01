import socket
from threading import Thread


def send(sock):
    while True:
        msg = input("请输入: ")
        sock.send(msg.encode('utf-8'))


def recv(sock):
    while True:
        msg = sock.recv(1024).decode('utf-8')
        print(msg)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8080))


p = Thread(target=send, args=(sock,))
t = Thread(target=recv, args=(sock,))
p.start()
t.start()