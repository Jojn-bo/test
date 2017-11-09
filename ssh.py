import paramiko

#创建ssh对象
ssh = paramiko.SSHClient
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko .AutoAddPolicy())
#连接服务器
ssh.connect(hostname='cl.salt.com',port=22,username='wupeiqi',password='123')

#执行命令
stdin,stdout,stderr = ssh.exec_command('df')
#获取命令结果
res,err = stdout.read(),stderr.read()
result = res if res else err


#关闭链接
ssh.close()
