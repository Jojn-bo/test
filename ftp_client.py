import socket
import os
import json

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()
    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
    def connect(self,ip,port):
        self.client.connect((ip, port))
    def interactive(self):
        #self.authenticate()
        while True:
            cmd = input('>>:').strip()
            if len(cmd) == 0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,'cmd_%s'%cmd_str):
                func = getattr(self,'cmd_%s'%cmd_str)
                func(cmd)
            else:
                self.help()
    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                # msg_str = '%s|%s'%(filename,filesize)
                msg_dic = {
                    'action':'put',
                    'filename': filename,
                    'size': filesize,
                    'overridden': True,
                    'iscat':True
                }
                self.client.send(json.dumps(msg_dic).encode())
                print('send',json.dumps(msg_dic).encode())
                # 防止黏包，等服务器确认
                server_response = self.client.recv(1024)
                print('回复是：',server_response)
                # flag = json.loads(server_response)
                # print('回复是：',flag['iscat'])
                f = open(filename, 'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print('file upload success...')
                    f.close()
            else:
                print(filename, 'is not exist')
    def cmd_get(self):
        pass

ftp = FtpClient()
ftp.connect('localhost',5000)
ftp.interactive()

