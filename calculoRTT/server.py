#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os

udpIP = "127.0.0.1"
updPort = 4006

updPortSend = 3003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Faz o bind local. Associa um socket com um IP e uma Porta.
sock.bind((udpIP, updPort))


while True:
    message, addr = sock.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
    print("Mensagem recebida: ", message)

    sock.sendto(message, (addr[0], updPortSend))
    # sock_client.sendto(message, (udpIP, updPortSend))

sock.close()
