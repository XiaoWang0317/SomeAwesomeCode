import pickle
import socket

import Utility as u

import BF as bf

PORT = 5050
SERVER = "127.0.0.1"
nodes = ['u', 'v', 'w', 'x', 'y', 'z']
distance_info_table = {}
router = []
network_size = 0
vector_table = {}

# set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER, PORT))
print(f"[LISTENING] server is listening on {SERVER} ")

# listen from the routers
while True:
    message, address = server_socket.recvfrom(2048)
    message = pickle.loads(message)
    router.append(address)

    # Accepting JOIN requirements
    if message.type == 1:
        print(f"JOIN {network_size}")

        # put the distance information into the table
        distance_info_table.update({message.name: message.data})
        network_size += 1

        # when there is 6 router, the network is built up, do Bellman ford
        if network_size == 6:
            g = bf.Graph(6)
            for key in distance_info_table.keys():
                dis_list = distance_info_table.get(key)
                for tuple in dis_list:
                    g.add_edge(key, tuple[0], tuple[1])
            vector_table = g.getTable(nodes)

            # write the vector table into distance.txt
            with open('distance.txt', 'w') as data:
                data.write(str(vector_table))

            # sent the note to lt every router knows the network is set up and sent the table
            index = 1
            for addr in router:
                reply = pickle.dumps(u.Packet(0, "server", "The network is set up \n" + str(vector_table)))
                server_socket.sendto(reply, addr)
                index += 1

    # Accepting modify requirement (Acceptable only after the network is set up)
    elif message.type == 2 and network_size == 6:
        print("UPDATE")

        # Change the distance information
        word = next(iter(message.data))
        new_list = message.data.get(word)
        distance_info_table.update(message.data)
        mod_dict = {}
        for tuple in new_list:
            mod_dict.update({tuple[0]: tuple[1]})

        for tuple in new_list:
            cur_list = distance_info_table.get(tuple[0])
            for i in range(0, len(cur_list)):
                if cur_list[i][0] == word:
                    cur_list[i] = (word, mod_dict.get(tuple[0]))

        # run bellman ford again
        g = bf.Graph(6)
        for key in distance_info_table.keys():
            dis_list = distance_info_table.get(key)
            for tuple in dis_list:
                g.add_edge(key, tuple[0], tuple[1])
        new_vector_table = g.getTable(nodes)

        # write the new vector table into new_distance.txt
        with open('new_distance.txt', 'w') as data:
            data.write(str(new_vector_table))

        # send modified vector table to every router
        index = 1
        for addr in router:
            reply = pickle.dumps(u.Packet(0, "server", "The network is updated \n" + str(new_vector_table)))
            server_socket.sendto(reply, addr)
            index += 1

    # Handle the error and halt the program
    else:
        print("ERROR")
        reply = pickle.dumps(u.Packet(0, "server", "ERROR occurred"))
        server_socket.sendto(reply, address)

    # when network set up, send to all routers
