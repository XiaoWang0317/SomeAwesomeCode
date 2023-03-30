import sys
from RDTSocket import RDTSocket

# PORT = 5050
# SERVER = "127.0.0.1"
# file = 'alice.txt'
SERVER = str(sys.argv[1])
file = 'download.txt'
PORT = int(sys.argv[2])
# window_size = 3
window_size = int(sys.argv[3])

# start the connection
client = RDTSocket(SERVER, PORT)
client.connect()
start_pkt_from_server = client.recv(2048)
seq_num = start_pkt_from_server.PacketHeader.seq_num
print(f"ACK seq# is {start_pkt_from_server.PacketHeader.seq_num}")

with open(file) as f:
    message = f.readlines()

i = 0

while i < len(message):
    msg = message[i]
    client.sendto(msg, client.ADDR, seq_num)
    pkt_from_server = client.recv(2048)
    seq_num = pkt_from_server.PacketHeader.seq_num
    if pkt_from_server.PacketHeader.type == 3:
        print(f"ACK seq# is {pkt_from_server.PacketHeader.seq_num}")
        i += pkt_from_server.data
        continue
    else:
        print("Error sent from server")
        break

client.close()

pkt_from_server = client.recv(2048)
if pkt_from_server.PacketHeader.type == 3:
    print("Finish!")
    client.socket.close()
