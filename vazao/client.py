#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

TCP_IP = '192.168.0.120'
TCP_PORT = 4004

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criando socket

sock.connect((TCP_IP, TCP_PORT)) # Abrindo conexão

messageFile = open("message_file")
message = messageFile.read() # Lendo mensagem do arquivo

sumBytes = 0
startTime = time.time() # Tempo inicial

for i in range(1000):
    print("Enviando mensagem...")
    sock.send(message.encode()) # Enviando mensagem

    data = sock.recv(1024) # Tamanho do buffer

    sumBytes += len(data) # Somando ao "sumBytes" o tamanho da mensagem de resposta do servidor

    time.sleep(0.1)
    # print("\nMensagem recebida: ", data)

endTime = time.time() # Tempo final

throughput = (((sumBytes * 8) / (endTime - startTime)) / 1000000)

print( "\nVazao: ", throughput, "Mb/s\n")

sock.close()


# outro programa com TCP
# mandar 12 megas e o time de fora do for
# mega(bytes) * 8/ tempo total gasto mb/s divide por milhao pra dar mega bits
# colocar sleep dentro do for pra nao mandar as 200 de uma vez