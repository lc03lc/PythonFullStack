import socket

client = socket.socket()
client.connect(('127.0.0.1', 8001))

reply = client.recv(1024).decode('utf-8')
print(reply)

while True:
    user = input('请输入用户名: ')
    if user.upper() == 'Q':
        break
    psd = input('请输入密码: ')
    client.sendall(user.encode('utf-8'))
    client.sendall(psd.encode('utf-8'))
    info = client.recv(1024).decode('utf-8')
    print(info)
    if info == '登录成功':
        break

client.close()
