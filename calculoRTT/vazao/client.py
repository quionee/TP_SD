#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

# IP LORENA: 192.168.0.103
# IP JOSEANE: 192.168.100.9

print("INICIO")

# 192.168.0.131
TCP_IP = '192.168.0.116'
TCP_PORT = 6667

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))

messageFile = open("message_file")
message = messageFile.read()
# message = "1"

sumBytes = 0
startTime = float(time.time())

for i in range(1000):
    print("RODANDO ", i)
    s.send(message.encode())

    data = s.recv(1024) # Tamanho do buffer.

    sumBytes += len(data)

    time.sleep(0.5)
    # print("\nMensagem recebida: ", data)

endTime = time.time()

# outro programa com TCP
# mandar 12 megas e o time de fora do for
# mega(bytes) * 8/ tempo total gasto mb/s divide por milhao pra dar mega bits
# colocar sleep dentro do for pra nao mandar as 200 de uma vez

throughput = (((sumBytes * 8) / (endTime - startTime)) / 1000000)

print( "\nVazao: ", throughput, "Mb/s\n")

s.close()