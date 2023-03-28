import Utility


from RDTSocket import RDTSocket

PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

server = RDTSocket(SERVER, PORT)
server.bind()
print(f"[LISTENING] server is listening on {SERVER} ")
message_list = []

while True:
    message, address = server.recvfrom(2048)
    if message.PacketHeader.type == 0:
        server.accept(address)
        print("[START]Connect sat up!---------------------")
    elif message.PacketHeader.type == 2 and server.connection_flag:
        # check the checksum
        if not Utility.check_checksum(message.data, message.PacketHeader.checksum):
            print("error")
            continue

        message_list.append(message.data)
        server.sendACK(message.PacketHeader.seq_num, address)
        print("================================================================================================================")
        print(f"[SEQUENCE] Sequence number is {message.PacketHeader.seq_num}")
        print(f"[RECEIVE]Message from Client:\n {message.data}")
        print(f"[ADDRESS]Client IP Address:{address}")
    elif message.PacketHeader.type == 1 and server.connection_flag:
        server.sendACK(-1, address)
        with open('download.txt', 'w') as f:
            for msg in message_list:
                f.writelines(msg)
            f.close()

