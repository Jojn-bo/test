import socket
import os

server = socket.socket()
server.bind(('localhost',6969))#绑定要监听的端口
server.listen()#监听

print('我要开始等电话了')
while True:
    conn,addr = server.accept()#等电话打进来
    print(conn,addr)
    # conn就是客户端连过来而在服务器端为其生成的一个链接实例
    print('电话来了')

    while True:
        data = conn.recv(1024).decode()
        if not data:
            print('%s 已断开链接',addr)
            break

        res = os.popen(data).read()
        if res == 0:
            continue
        conn.send(res.encode())

server.close()