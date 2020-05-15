#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

TCP_IP = ''
TCP_PORT = 4004

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criando socket

sock.connect((TCP_IP, TCP_PORT)) # Abrindo conexão

messageFile = open("message_file")
message = messageFile.read() # Lendo mensagem do arquivo
messageFile.close()

sumBytes = 0
startTime = time.time() # Tempo inicial

for i in range(10000):
    sock.send(message.encode()) # Enviando mensagem
    sumBytes += len(message)

sock.close()

endTime = time.time() # Tempo final

throughput = (((sumBytes * 8) / (endTime - startTime)) / 1000000)

print( "\nVazao: ", throughput, "Mb/s\n")
