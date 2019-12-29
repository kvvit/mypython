#!/usr/bin/env python3
import socket
import subprocess
import sys
from datetime import datetime

remoteServer = "vcenter.ad.pu.ru"
remoteServerIP = socket.gethostbyname(remoteServer)

remoteServerIP_splitted = remoteServerIP.split('.')
print(remoteServerIP_splitted[0])
print(remoteServerIP_splitted[1])
print(remoteServerIP_splitted[2])
print(remoteServerIP_splitted[3])

print('IP addess is: ', remoteServerIP)
port = 22

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket is: ', sock)
result = sock.connect_ex((remoteServerIP, port))

if result == 0:
    print("Port {}:    Open".format(port))
sock.close()


print('result is: ', result)