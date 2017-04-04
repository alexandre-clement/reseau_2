#!/usr/bin/env python
# coding: utf-8

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send(u"GET /index.html HTTP/1.1")

while True:
    msg = socket.recv(1024)
    if len(msg) != 0:
        print msg

print "Close"
socket.close()
