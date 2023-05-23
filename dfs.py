from collections import defaultdict, deque

# Recursive Depth First Search (DFS) algorithm
def dfs_recursive(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Depth First Search (DFS) algorithm
def dfs(graph, start):
    visited = set()
    dfs_recursive(graph, start, visited)

# Breadth First Search (BFS) algorithm
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main code
graph = defaultdict(list)

# Allowing the user to input the graph
num_vertices = int(input("Enter the number of vertices in the graph: "))
num_edges = int(input("Enter the number of edges in the graph: "))

print("Enter the edges in the format 'vertex1 vertex2':")
for _ in range(num_edges):
    v1, v2 = input().split()
    graph[v1].append(v2)
    graph[v2].append(v1)

start_vertex = input("Enter the starting vertex for DFS and BFS: ")

print("Depth First Search (DFS):")
dfs(graph, start_vertex)
print("\nBreadth First Search (BFS):")
bfs(graph, start_vertex)
