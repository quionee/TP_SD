#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
import time

# Dados do cliente
udp_ip = "127.0.0.1"
udp_port = 3003

# Dados do servidor
udp_ip_send = "127.0.0.1"
udp_port_send = 4004

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
# sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(0.00001)

# Faz o bind local. Associa um socket com um IP e uma Porta.
sock.bind((udp_ip, udp_port))

sumRTT = 0
numberOfPackages = 100
numberOfPackagesLost = 0

messageFile = open("message_file")
message = messageFile.read()

for i in range(numberOfPackages):
    startTime = float(time.time())
    sock.sendto(message.encode(), (udp_ip_send, udp_port_send))

    try:
        recv_message = sock.recvfrom(1024)
    except Exception as e:
        if e.code == -1007:
            print("\n\nestourou timeout, perdeu pacote\n\n")

    # except sock.timeout:
    #     numberOfPackagesLost += 1
    #     print("\n\nPERDEU PACOTE\n\n")

    endTime = time.time()
    # time.sleep(5)
    if (recv_message != ""):
        RTT = endTime - startTime
        sumRTT += RTT
        # print ("Mensagem recebida: ", recv_message)

numberOfPackagesSent = numberOfPackages - numberOfPackagesLost
RTT = sumRTT / numberOfPackagesSent
print("\nRTT: ", RTT)