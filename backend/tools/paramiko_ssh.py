import paramiko
import time


class ParamikoSSH:
    def __init__(self,hostname,port,username,password) -> None:
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.ssh = None
        self.channel = None

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.hostname,self.port,self.username,self.password)
        self.channel = self.ssh.invoke_shell()

    def send_command(self,command):
        if self.channel:
            self.channel.send(command + '\n')
        else:
            raise Exception("没有活跃的channel")

    def read_output(self,sleep_time=1):
        try:
            while True:
                if self.channel.recv_ready():
                    output = self.channel.recv(8192).decode('utf-8')
                    print(output,end="")
                    return output
                time.sleep(sleep_time)
        except KeyboardInterrupt:
            print("用户键盘中断")

    def close(self):
        if self.channel:
            self.channel.close()
        if self.ssh:
            self.ssh.close()

paramiko_instance = ParamikoSSH("connect.beijinga.seetacloud.com",46786,'root','peDyj80Rw6ih')

# ssh -p 46786 root@connect.beijinga.seetacloud.com
if __name__ == '__main__':
    hostname = "connect.beijinga.seetacloud.com"
    port = 46786
    username = 'root'
    password = 'peDyj80Rw6ih'

    client = ParamikoSSH(hostname,port,username,password)
    client.connect()
    client.send_command('ls')
    client.read_output()
    client.close()
