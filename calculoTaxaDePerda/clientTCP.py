#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5012

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while True:
    message = input('Digite Sua Mensagem: ')

    startTime = float(time.time())

    s.send(message.encode())

    endTime = s.recv(1024) # Tamanho do buffer.

    endTimeRTT = time.time()

    totalTime = str(float(endTime) - startTime)

    print("\nRTT: ", endTimeRTT - startTime, "\nLatency: ", totalTime, "\n")

s.close()