import socket
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

PORT = 47590
SERVER = '127.0.0.1'

http = str(sys.argv[1])
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER, PORT))

while True:
    client_socket.send(http.encode())
    msg = client_socket.recv(204800).decode()
    with open('text.txt', 'w') as data:
        data.write(str(msg))
    print(msg)
