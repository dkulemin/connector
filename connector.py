import paramiko
import getpass
import sys

print("Enter host list:", end=' ')
hosts = input()
#login = input()
#passwd = input()
#port = 22

for host in list(hosts.split(',')):
    print("login:", end=' ')
    login = input()
    #print("password:", end=' ')
    #passwd = input()
    passwd = getpass.getpass()
    port = 22
    try:
        ### Taken from https://habr.com/post/150047/
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=login, password=passwd, port=port)
        stdin, stdout, stderr = client.exec_command('ls -la')
        data = stdout.read() + stderr.read()
        client.close()
        ### end
        print(data.decode('utf-8'))
    except Exception as e:
        print("SSH connection error: {0}".format(e))