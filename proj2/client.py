
from RDTSocket import RDTSocket

PORT = 5050
SERVER = "127.0.0.1"
# ADDR = (SERVER, PORT)

# start the connection
client = RDTSocket(SERVER, PORT)
client.connect()
start_pkt_from_server = client.recv(2048)
seq_num = start_pkt_from_server.PacketHeader.seq_num
print(f"ACK seq# is {start_pkt_from_server.PacketHeader.seq_num}")

with open('alice.txt') as f:
    message = f.readlines()

for i in range(len(message)):
    msg = message[i]
    seq_num += 1
    client.sendto(msg, client.ADDR, seq_num)
    # pkt_from_server = pickle.loads(client.recv(4096))
    pkt_from_server = client.recv(2048)
    seq_num = pkt_from_server.PacketHeader.seq_num
    if pkt_from_server.PacketHeader.type == 3:
        print(f"ACK seq# is {pkt_from_server.PacketHeader.seq_num}")
        continue
    else:
        print("Error occur")
        break

client.close()

pkt_from_server = client.recv(2048)
if pkt_from_server.PacketHeader.type == 3:
    print("Finish!")
    client.close()
