# Bellman Ford Algorithm in Python


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Total number of vertices in the graph
        self.graph = []  # Array of edges
        self.dict = {'u': 0, 'v': 1, 'w': 2, 'x': 3, 'y': 4, 'z': 5}
        self.table = {}

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([self.dict.get(s), self.dict.get(d), w])
        self.graph.append([self.dict.get(d), self.dict.get(s), w])

    # Print and store the solution
    def print_solution(self, dist, source):
        print("Vertex Distance from ", source)
        dis_list = []
        for i in range(self.V):
            word = list(self.dict.keys())[i]
            print("{0}\t\t{1}".format(word, dist[i]))
            if word != source:
                dis_list.append((word, dist[i]))
            self.table.update({source: dis_list})

    def bellman_ford(self, src):
        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[self.dict.get(src)] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist, src)

    # run the bellman ford and get the vector table
    def getTable(self, nodes):
        for n in nodes:
            self.bellman_ford(n)
        return self.table


if __name__ == '__main__':
    dict = {'v': [('w', 3), ('y', 4), ('u', 7)],
            'u': [('x', 5), ('w', 3), ('v', 7)],
            'w': [('v', 3), ('y', 8), ('u', 3), ('x', 4)],
            'x': [('u', 5), ('w', 4), ('z', 9), ('y', 7)],
            'y': [('x', 7), ('z', 2), ('v', 4), ('w', 8)],
            'z': [('y', 2), ('x', 9)]}

    g = Graph(6)
    for key in dict.keys():
        dis_list = dict.get(key)
        for tuple in dis_list:
            g.add_edge(key, tuple[0], tuple[1])

    nodes = ['u', 'v', 'w', 'x', 'y', 'z']
    print(g.getTable(nodes))
