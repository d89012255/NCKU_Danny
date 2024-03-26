# -*- coding: utf-8 -*-
import socket
HOST = '192.168.50.136'
PORT = 2350

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = conn.recv(4194304)


    f = open("QQQ.mp3", "wb")
    f.write(clientMessage)
    f.close()

    serverMessage = '下一筆'
    conn.send(serverMessage.encode())
    conn.close()