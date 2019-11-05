#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/7 11:49
"""
import socket

HOST = '127.0.0.1'
PORT = 8085
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = "GET / HTTP/1.1 \r\nHOST 127.0.0.1:8085\r\n"

s.send(data.encode('utf-8'))
data = s.recv(1024)
print('Received :', repr(data))
s.close()
