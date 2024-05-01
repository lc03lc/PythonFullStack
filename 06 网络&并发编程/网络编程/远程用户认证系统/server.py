import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    conn.sendall("欢迎使用xx系统".encode('utf-8'))

    while True:
        user = conn.recv(1024).decode('utf-8')
        if not user:
            break
        psd = conn.recv(1024).decode('utf-8')

        with open('user.txt', mode='r') as f:
            if " ".join([user, psd]) in [x.strip() for x in f.readlines()]:
                conn.sendall('登录成功'.encode('utf-8'))
                print("{}成功登录系统".format(user))
                break

        conn.sendall('登录失败，请重试，(Q/q退出)'.encode('utf-8'))
        print("{}未成功登录系统".format(user))

    conn.close()

sock.close()
