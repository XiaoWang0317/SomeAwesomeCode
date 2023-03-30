import pickle
import Utility, socket


class RDTSocket(Utility.UnreliableSocket):
    def __init__(self, ip, port):
        self.connection_flag = False
        self.ADDR = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def accept(self, address, window_size):
        self.connection_flag = True
        self.sendACK(0, address, window_size)

    def connect(self):
        start_pkt = pickle.dumps(Utility.makeStart(0, "10100101"))
        self.socket.sendto(start_pkt, self.ADDR)

    def sendto(self, data, address, seq_num):
        header = Utility.PacketHeader(2, seq_num, len(data), Utility.getCheckSum(data))
        data = Utility.Packet(header, data)
        data = pickle.dumps(data)
        self.socket.sendto(data, address)

    def recvfrom(self, size):
        pkt, address = self.socket.recvfrom(size)
        return pickle.loads(pkt), address

    def sendACK(self, seq_num, address, data):
        ack_pkt = pickle.dumps(Utility.makeAck(seq_num, 000000000, data))
        self.socket.sendto(ack_pkt, address)

    def recv(self, size):
        pkt = self.socket.recv(size)
        return pickle.loads(pkt)

    def close(self):
        end_pkt = pickle.dumps(Utility.makeEnd(10000, 000000000))
        self.socket.sendto(end_pkt, self.ADDR)



