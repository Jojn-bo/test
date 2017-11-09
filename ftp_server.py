import socketserver
import json,os

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote:'.format(self.client_address[0]))
                print('self.data:',self.data)
                cmd_dic = json.dumps(self.data).encode()
                print('cmd_dic:',cmd_dic)
                #action = cmd_dic['action']
                if hasattr(self, cmd_dic):
                    func = getattr(self, cmd_dic['action'])
                    func(cmd_dic)

            except ConnectionResetError as e:
                print('err:',e)
                break
    def put(self, *args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['size']
        if os.path.isfile(filename):
            f = open(filename + '.new','wb')
        else:
            f = open(filename, 'wb')

        cmd_dic['iscat'] = True
        self.request.send(json.dumps(cmd_dic).encode())
        receive_size = 0
        while receive_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            receive_size += len(data)
        else:
            print('file [%s] has uploaded...'% filename)


if __name__ == '__main__':
    HOST,PORT = 'localhost',5000
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()