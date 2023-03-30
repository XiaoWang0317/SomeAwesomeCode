import Utility
from RDTSocket import RDTSocket
import sys

# PORT = 5050
# SERVER = "127.0.0.1"
SERVER = str(sys.argv[1])
file = 'download.txt'
PORT = int(sys.argv[2])
# window_size = 3
window_size = int(sys.argv[3])
server = RDTSocket(SERVER, PORT)
server.bind()
print(f"[LISTENING] server is listening on {SERVER} ")
message_list = []
ack_list = []

while True:
    message, address = server.recvfrom(2048)
    if message.PacketHeader.type == 0:
        server.accept(address, window_size)
        print("[START]Connection sat up!---------------------")
    elif message.PacketHeader.type == 2 and server.connection_flag:
        # check the checksum
        if not Utility.check_checksum(message.data, message.PacketHeader.checksum):
            server.sendACK(message.PacketHeader.seq_num, address, -window_size)
            ack_list.append(0)
            print("error")
            continue
        ack_list.append(1)
        message_list.append(message.data)
        if len(ack_list) > window_size and ack_list[len(ack_list) - window_size] == 0:
            server.sendACK(message.PacketHeader.seq_num + 1, address, window_size * (-1))
            ack_list = ack_list[:window_size * (-1)]
            message_list = message_list[:window_size * (-1)]
        else:
            server.sendACK(message.PacketHeader.seq_num + 1, address, 1)
            print("================================================================================================================")
            print(f"[SEQUENCE] Sequence number is {message.PacketHeader.seq_num}")
            print(f"[RECEIVE]Message from Client:\n {message.data}")
            print(f"[ADDRESS]Client IP Address:{address}")
    elif message.PacketHeader.type == 1 and server.connection_flag:
        for i in range(len(ack_list) - window_size, len(ack_list) - 1):
            if len(ack_list) > window_size and ack_list[len(ack_list) - window_size] == 0:
                server.sendACK(message.PacketHeader.seq_num + 1, address, window_size * (-1))
                ack_list = ack_list[:window_size * (-1)]
                message_list = message_list[:window_size * (-1)]
                break
        server.sendACK(-1, address, 0)
        with open(file, 'w') as f:
            for msg in message_list:
                f.writelines(msg)
            f.close()


