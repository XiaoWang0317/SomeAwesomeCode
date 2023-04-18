

class Packet:
    def __init__(self, type, name, data):
        self.type = type    # 1 for join, 2 for modify
        self.name = name    # name of the packet sender
        self.data = data    # data to be sent
