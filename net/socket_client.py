#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/7 11:49
"""
import socket

HOST = '127.0.0.1'
PORT = 8085

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'hello world.')
    data = s.recv(1024)

print('Received :', repr(data))
