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
udp_port_send = 4006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
# sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(0.00000000001)

# Faz o bind local. Associa um socket com um IP e uma Porta.
sock.bind((udp_ip, udp_port))

sumRTT = 0
numberOfPackages = 200
numberOfPackagesLost = 0

messageFile = open("message_file")
message = messageFile.read()

sumBytes = 0

for i in range(numberOfPackages):
    startTime = float(time.time())
    sock.sendto(message.encode(), (udp_ip_send, udp_port_send))

    try:
        recv_message = sock.recvfrom(1024)
        sumBytes += len(recv_message)
    except Exception:
        numberOfPackagesLost += 1

    endTime = time.time()
    if (recv_message != ""):
        rtt = endTime - startTime
        sumRTT += rtt
        # print ("Mensagem recebida: ", recv_message)

numberOfPackagesSent = numberOfPackages - numberOfPackagesLost

rtt = sumRTT / numberOfPackagesSent
throughput = (((sumBytes * 8) * 0.001) / rtt)
lossRate = (numberOfPackagesLost / numberOfPackages) * 100

print("\nRTT: ", rtt)
print("\nVazão: ", throughput)
print("\nQuantidade de pacotes perdidos: ", numberOfPackagesLost)
print("\nTaxa de perda: ", lossRate, "%")