class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        for edge in self.graph:
            src, dest, weight = edge

            if self.find(parent, src) != self.find(parent, dest):
                result.append(edge)
                self.union(parent, rank, src, dest)

        return result


# User input for the number of vertices in the graph
num_vertices = int(input("Enter the number of vertices in the graph: "))

g = Graph(num_vertices)

# User input for the edges of the graph
num_edges = int(input("Enter the number of edges in the graph: "))

print("Enter the source, destination, and weight of each edge:")

for i in range(num_edges):
    src, dest, weight = map(int, input().split())
    g.add_edge(src, dest, weight)

# Find the minimum spanning tree using Kruskal's algorithm
mst = g.kruskal_mst()

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for src, dest, weight in mst:
    print(f"Source: {src}  Destination: {dest}  Weight: {weight}")
