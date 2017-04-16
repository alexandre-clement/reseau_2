import socket
import os
import re
import subprocess
import unicodedata
import sys

ROOT_PATH = r"C:\Users\user\Desktop\server\root"
os.environ["ROOT_PATH"] = ROOT_PATH
INDEX = "index.html"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverPort = 15555
serverSocket.bind(("", serverPort))

serverSocket.listen(1)

while True:
    connectionSocket, address = serverSocket.accept()

    message = connectionSocket.recv(1024)
    if message is None or message == "":
        continue

    # print "\nmessage :\n", message, "\nend message\n"

    matcher = re.search("(GET|POST) /([^ ?]*)(?:\?([^ ]*))? HTTP/1.1", message)

    method = matcher.group(1)
    url = matcher.group(2)
    arguments = matcher.group(3)
    body = re.search("(?m)Content-Length:\s*(\d+)\s+((?:.|\s)*)", message)

    # print method, url, arguments

    try:
        os.environ["QUERY_STRING"] = ""
        if url.startswith("cgi-bin"):
            if method.upper() == "GET":
                os.environ["QUERY_STRING"] = arguments
                subprocess.call(str.format("python {}".format(os.path.join(ROOT_PATH, url))), stdout=open("tmp", "w"))
            elif method.upper() == "POST":
                with open("tmp_stdin", "w") as stdout:
                    stdout.write(body.group(2))
                subprocess.call(str.format("python {}".format(os.path.join(ROOT_PATH, url))), stdin=open("tmp_stdin"), stdout=open("tmp", "w"))
            page = open("tmp")
        else:
            page = open(os.path.join(ROOT_PATH, url))
        os.environ["QUERY_STRING"] = ""
    except (IOError, AttributeError), error:
        print error
        page = open(os.path.join(ROOT_PATH, INDEX))

    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

    connectionSocket.send(page.read())
    page.close()

    connectionSocket.send("\r\n")
    connectionSocket.close()

serverSocket.close()