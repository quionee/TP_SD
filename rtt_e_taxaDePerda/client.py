#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cálculo do RTT e da Taxa de Perda

import socket
import os
import time

# Dados do cliente
udp_ip = "192.168.0.131"
udp_port = 3003

# Dados do servidor
udp_ip_send = "192.168.0.116"
udp_port_send = 4006

sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

sockUDP.settimeout(0.1)

# Faz o bind local. Associa um socket com um IP e uma Porta.
sockUDP.bind((udp_ip, udp_port))

sumRTT = 0
numberOfPackages = 1000
numberOfPackagesLost = 0

message = "a mensagem aqui"

rtt = 0

startTime = float(time.time())

try:
    sockUDP.sendto(message.encode(), (udp_ip_send, udp_port_send))
except Exception:
    print(" ----- timeout de envio ----- ")

messageReceived = ""

try:
    messageReceived = sockUDP.recvfrom(1024)
except Exception:
    print(" ----- timeout de recebimento ----- ")

endTime = time.time()

if (messageReceived != ""):
    rtt = endTime - startTime
    # print ("Mensagem recebida: ", messageReceived)

# ----- CÁLCULO DO RTT MÉDIO E TAXA DE PERDA

sockUDP.settimeout(0.01)

sumBytes = 0
startTime = float(time.time())

for i in range(numberOfPackages):

    try:
        sockUDP.sendto(message.encode(), (udp_ip_send, udp_port_send))
    except Exception:
        print(" ----- timeout de envio ----- ")

    messageReceived = ""

    try:
        messageReceived = sockUDP.recvfrom(1024)
    except Exception:
        numberOfPackagesLost += 1
        print(" ----- timeout de recebimento ----- ")

    endTime = time.time()

    if (messageReceived != ""):
        sumRTT = endTime - startTime
        # print ("Mensagem recebida: ", messageReceived)

numberOfPackagesSent = numberOfPackages - numberOfPackagesLost

meanRTT = sumRTT / numberOfPackagesSent
lossRate = (numberOfPackagesLost / numberOfPackages) * 100

print("\nRTT: ", rtt, "s")
print("\nRTT médio: ", meanRTT, "s")
print("\nTaxa de perda: ", lossRate, "%")
print("\nQuantidade de pacotes perdidos: ", numberOfPackagesLost)

# remover vazão
# string de 10 caracteres por exemplo
# assim está pronto rtt e taxa de perda