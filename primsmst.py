import heapq

def prim_minimum_spanning_tree(graph):
    start_vertex = list(graph.keys())[0]
    visited = set([start_vertex])
    min_spanning_tree = []
    edges = [
        (weight, start_vertex, neighbor)
        for neighbor, weight in graph[start_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            min_spanning_tree.append((u, v, weight))

            for neighbor, edge_weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_weight, v, neighbor))

    return min_spanning_tree

# User input for graph
graph = {}
num_vertices = int(input("Enter the number of vertices: "))

for i in range(num_vertices):
    vertex = input(f"Enter the vertex {i+1}: ")
    graph[vertex] = {}

    num_neighbors = int(input(f"Enter the number of neighbors for {vertex}: "))
    for j in range(num_neighbors):
        neighbor, weight = input(f"Enter neighbor {j+1} and its weight: ").split()
        graph[vertex][neighbor] = int(weight)

        # Add the neighbor vertex to the graph if not present
        if neighbor not in graph:
            graph[neighbor] = {}

        # Assuming undirected graph, assign weight to both directions
        graph[neighbor][vertex] = int(weight)
        graph[vertex][neighbor] = int(weight)

# Print the user-input graph
print("Graph:")
for vertex, neighbors in graph.items():
    print(vertex + ":", neighbors)

# Compute minimum spanning tree
mst = prim_minimum_spanning_tree(graph)

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")

