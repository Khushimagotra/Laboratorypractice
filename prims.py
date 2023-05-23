import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def find_min_key(self, key, mst_set):
        min_key = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_key and not mst_set[v]:
                min_key = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.find_min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def print_mst(self, parent):
        print("Minimum Spanning Tree:")
        for v in range(1, self.V):
            print(f"Edge: {parent[v]} - {v}  Weight: {self.graph[v][parent[v]]}")


# User input for the number of vertices in the graph
num_vertices = int(input("Enter the number of vertices in the graph: "))

g = Graph(num_vertices)

# User input for the edges of the graph
num_edges = int(input("Enter the number of edges in the graph: "))

print("Enter the source, destination, and weight of each edge:")

for _ in range(num_edges):
    src, dest, weight = map(int, input().split())
    g.add_edge(src, dest, weight)

# Find the minimum spanning tree using Prim's algorithm
mst_parent = g.prim_mst()

# Print the minimum spanning tree
g.print_mst(mst_parent)
