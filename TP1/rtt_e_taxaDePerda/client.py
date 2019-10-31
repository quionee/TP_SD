#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----- CÁLCULO DO RTT -----

import socket
import os
import time

# Dados do cliente
udp_ip = "192.168.103.5"
udp_port = 3003

# Dados do servidor
udp_ip_send = "192.168.103.4"
udp_port_send = 4006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria socket

sock.settimeout(0.1) # Determina timeout

sock.bind((udp_ip, udp_port)) # Associa um socket com um IP e uma porta

message = "A computacao na tomada de decisoes"

# rtt = 0

# startTime = time.time() # Tempo inicial

# try:
#     sock.sendto(message.encode(), (udp_ip_send, udp_port_send)) # Envia mensagem
# except Exception:
#     print(" ----- timeout de envio ----- ")

# messageReceived = ""

# try:
#     messageReceived = sock.recvfrom(1024) # Recebe mensagem
# except Exception:
#     print(" ----- timeout de recebimento ----- ")

# endTime = time.time() # Tempo final

# if (messageReceived != ""):
#     rtt = endTime - startTime
#     # print("Mensagem recebida: ", messageReceived)


# ----- CÁLCULO DO RTT MÉDIO E TAXA DE PERDA -----

sock.settimeout(0.1) # Determina timeout

sumRTT = 0
numberOfPackages = 30
numberOfPackagesLost = 0
sumBytes = 0

for i in range(numberOfPackages):
    startTime = time.time() # Tempo inicial
    try:
        sock.sendto(message.encode(), (udp_ip_send, udp_port_send)) # Envia pacote
    except Exception:
        print(" ----- timeout de envio ----- ")

    messageReceived = ""

    try:
        messageReceived = sock.recvfrom(1024) # Recebe mensagem
    except Exception:
        numberOfPackagesLost += 1 # Incrementa números de pacotes perdidos caso haja perda
        print(" ----- timeout de recebimento ----- ")

    endTime = time.time() # Tempo final

    if (messageReceived != ""):
        sumRTT += endTime - startTime
        # print("Mensagem recebida: ", messageReceived)

    time.sleep(0.5)

numberOfPackagesSent = numberOfPackages - numberOfPackagesLost

meanRTT = sumRTT / numberOfPackagesSent # Cálcula o RTT médio
lossRate = (numberOfPackagesLost / numberOfPackages) * 100 # Calcula a taxa de perda (porcentagem)

sock.close()

# print("\nRTT: ", rtt, "s")
print("\nRTT médio: ", meanRTT, "s")
print("\nTaxa de perda: ", lossRate, "%")
print("\nQuantidade de pacotes perdidos: ", numberOfPackagesLost)