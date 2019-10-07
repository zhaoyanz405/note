#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/7 11:40
"""

import socket

HOST = '127.0.0.1'
PORT = 8085

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connect by', addr)
        d_list = []
        while True:
            data = conn.recv(1024)
            if not data:
                break

            d_list.append(data)
            conn.sendall(b'recv done')
    print('rece: ', d_list)
