import os
import re
import socket
os.chdir('/Users/Terry/Desktop')

# creat a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect sock with the web and port 80
mysock.connect(('data.pr4e.org',80))
# get the url use cmd
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()


