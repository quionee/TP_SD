#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cálculo do RTT e da Taxa de Perda

import socket
import os

udpIP = "192.168.100.9"
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

sockUDP.settimeout(0.01)

# Faz o bind local. Associa um socket com um IP e uma Porta.
sockUDP.bind((udp_ip, udp_port))

message = "a mensagem aqui"
rtt = 0

# for i in range(numberOfPackages):
startTime = float(time.time())

try:
    sockUDP.sendto(message.encode(), (udp_ip_send, udp_port_send))
except Exception:
    print(" ----- timeout de envio ----- ")

try:
    messageReceived = sockUDP.recvfrom(1024)
except Exception:
    print(" ----- timeout de recebimento ----- ")

endTime = float(time.time())

messageReceived = ""
if (messageReceived != ""):
    rtt = endTime - startTime
    # print ("Mensagem recebida: ", messageReceived)

print("\nRTT: ", rtt, "s")

sumRTT = 0
numberOfPackages = 100
numberOfPackagesLost = 0
sumBytes = 0
meanRTT = 0

for i in range(numberOfPackages):
    print("RODANDO", i)

    messageReceived = ""
    startTime = time.time()

    try:
        sockUDP.sendto(message.encode(), (udp_ip_send, udp_port_send))
    except Exception:
        print(" ----- timeout de envio ----- ")

    try:
        messageReceived = sockUDP.recvfrom(1024)
        sumBytes += len(messageReceived)
    except Exception:
        numberOfPackagesLost += 1
        print(" ----- timeout de recebimento ----- ")

    endTime = time.time()
    messageReceived = ""
    if (messageReceived != ""):
        meanRTT = endTime - startTime
        sumRTT += meanRTT
        # print ("Mensagem recebida: ", messageReceived)

numberOfPackagesSent = numberOfPackages - numberOfPackagesLost

lossRate = (numberOfPackagesLost / numberOfPackages) * 100

print("\nRTT: ", rtt, "s")
print("\nRTT medio: ", meanRTT, "s")
print("\nTaxa de perda: ", lossRate, "%")
print("\nQuantidade de pacotes perdidos: ", numberOfPackagesLost)

# remover vazão
# string de 10 caracteres por exemplo
# assim está pronto rtt e taxa de perda