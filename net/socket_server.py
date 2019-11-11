#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/7 11:40
"""
import datetime
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8085))
s.listen()
conn, addr = s.accept()


def parse(data):
    """

    :param data:
    :return:
    """
    _dict = {}
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    pairs = data.split('\r\n')

    request_line = pairs[0].split(' ')
    _dict['method'] = request_line[0]
    _dict['url'] = request_line[1]
    _dict['http_version'] = request_line[2]
    _dict['header'] = pairs[1]

    return _dict


def handle(url):
    """

    :param url:
    :return:
    """
    if url != "/":
        status = 404
        status_msg = 'Not Found'
        content = 'oh no ! 404 happening.'
    else:
        status = 200
        status_msg = "OK"
        content = """<html>
              <head></head>
              <body>
                    <h1 class="color: green">success!</h1>
              </body>
        </html>
        """

    resonse = "HTTP/1.1 {status} {status_msg}\n" \
              "Date: {date}\n" \
              "Content-Type: text/html; charset=UTF-8\n" \
              "Content-Length: {length}\r\n" \
              "{content}\r\n".format(status=status, status_msg=status_msg,
                                     date=datetime.datetime.now(), length=len(content),
                                     content=content)
    return resonse.encode('utf-8')


with conn:
    print('Connect by', addr)
    d_list = []
    while True:
        data = conn.recv(128)
        if not data:
            break

        print(data)
        if data.decode('utf-8').find('\r\n\r\n'):
            break

s.close()
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connect by', addr)
#         d_list = []
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#
#             d_list.append(data)
#             conn.sendall(b'recv done')
#     print('rece: ', d_list)
