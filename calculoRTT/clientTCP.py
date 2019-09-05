#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5010

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while True:
    message = input('Digite Sua Mensagem: ')

    startTime = float(time.time())

    s.send(message.encode())

    data = s.recv(1024) #Tamanho do buffer.

    time.sleep(5)

    endTime = time.time()

    totalTime = str(endTime - startTime)

    print("\nMensagem recebida: ", data, "\nRTT: ", totalTime, "\n")

s.close()