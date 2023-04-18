import pickle
import socket
import sys
import Utility as u

PORT = 5050
SERVER = "127.0.0.1"

# distance information for each router
dict = {'u': [('x', 5), ('w', 3), ('v', 7)],
        'v': [('w', 3), ('y', 4), ('u', 7)],
        'w': [('v', 3), ('y', 8), ('u', 3), ('x', 4)],
        'x': [('u', 5), ('w', 4), ('z', 9), ('y', 7)],
        'y': [('x', 7), ('z', 2), ('v', 4), ('w', 8)],
        'z': [('y', 2), ('x', 9)]}

# modified distance information
mod = {'y': [('x', 7), ('z', 3), ('v', 4), ('w', 8)]}

name = str(sys.argv[1]) # router name
type = int(sys.argv[2]) # type of requirement
# start the connection
while True:
    # send requirement to join the network
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent_pkt = pickle.dumps(u.Packet(1, name, dict.get(name)))
    client_socket.sendto(sent_pkt, (SERVER, PORT))
    message = pickle.loads(client_socket.recv(2048))
    print(message.data)

    # send requirement to modify the network
    if type == 2:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent_pkt = pickle.dumps(u.Packet(type, name, mod))
        client_socket.sendto(sent_pkt, (SERVER, PORT))
    message = pickle.loads(client_socket.recv(2048))
    print(message.data)
    break



