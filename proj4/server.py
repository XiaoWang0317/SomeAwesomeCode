import socket
import requests

PORT = 47591
SERVER = '127.0.0.1'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER, PORT))
server_socket.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    http = client_socket.recv(2048).decode()
    reply = requests.get(http)

    print(reply.text)

    client_socket.send(bytes(reply.text, "utf-8"))
