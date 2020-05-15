#!/usr/bin/env python
# -- coding: utf-8 --

# ----- CÁLCULO DO RTT E TAXA DE PERDA -----

import socket
import os

udpIP = ""
updPort = 4006

updPortSend = 3003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criando socket

sock.bind((udpIP, updPort)) # Associando um socket com um IP e uma porta
print("Aguardando conexao...")

while True:
    message, addr = sock.recvfrom(1024) # Tamanho do buffer
    print("Mensagem recebida: ", message)

    sock.sendto(message, (addr[0], updPortSend))

sock.close()