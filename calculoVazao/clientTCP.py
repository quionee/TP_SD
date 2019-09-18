#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

message = input('Digite Sua Mensagem: ')
startTime = float(time.time())
sumBytes = 0

while (message != 'encerrar conexao'):
    s.send(message.encode())

    data = s.recv(1024) #Tamanho do buffer.
    sumBytes += len(data)

    print("\nMensagem recebida: ", data)
    endTime = time.time()
    message = input('Digite Sua Mensagem: ')

rtt = endTime - startTime

throughput = (((sumBytes * 8) * 0.001) / rtt)

print( "\nThroughput: ", rtt, "\n")

s.close()