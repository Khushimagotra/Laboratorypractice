from heapq import heappop, heappush


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    def dijkstra_shortest_path(self, src):
        # Initialize distances and visited array
        distances = [float('inf')] * self.V
        distances[src] = 0
        visited = [False] * self.V

        # Priority queue for selecting the next vertex
        pq = [(0, src)]

        while pq:
            dist, u = heappop(pq)
            visited[u] = True

            # Explore adjacent vertices
            for v, weight in self.graph[u]:
                if not visited[v] and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heappush(pq, (distances[v], v))

        return distances


# User input for the number of vertices in the graph
num_vertices = int(input("Enter the number of vertices in the graph: "))

g = Graph(num_vertices)

# User input for the edges of the graph
num_edges = int(input("Enter the number of edges in the graph: "))

print("Enter the source, destination, and weight of each edge:")

for i in range(num_edges):
    src, dest, weight = map(int, input().split())
    g.add_edge(src, dest, weight)

# User input for the source vertex to find the shortest path
source_vertex = int(input("Enter the source vertex: "))

# Find the shortest paths using Dijkstra's algorithm
shortest_paths = g.dijkstra_shortest_path(source_vertex)

# Print the shortest paths
print("Shortest Paths from the source vertex:")
for i, distance in enumerate(shortest_paths):
    print(f"Vertex {i}: Distance = {distance}")
