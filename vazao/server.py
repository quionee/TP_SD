#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

TCP_IP = '192.168.0.120'
TCP_PORT = 4004

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criando socket

sock.bind((TCP_IP, TCP_PORT)) # Associando socket ao endereço

sock.listen(1) # Aguardando conexão
print("Aguardando conexao...")
 
connection, address = sock.accept() # Aceitando conexão

while True:
    data = connection.recv(1024) # Tamanho do buffer
    print("Mensagem Recebida: ", data)
    message = data.upper()
    connection.send(message)  # echo

connection.close()
