def dijkstra(graph, source):
  """
  This function implements Dijkstra's single source shortest path algorithm.

  Args:
    graph: A graph represented as a list of lists. Each inner list represents
      the edges connected to a vertex.
    source: The source vertex.

  Returns:
    A dictionary that maps each vertex to its distance from the source vertex.
  """

  # Initialize the distances.
  distances = {}
  for vertex in graph:
    distances[vertex] = float("inf")

  # Initialize the set of visited vertices.
  visited = set()

  # Set the distance to the source vertex to 0.
  distances[source] = 0

  # While there are still vertices to visit:
  while len(visited) < len(graph):

    # Find the vertex with the minimum distance that is not yet visited.
    minimum_vertex = min(
        (vertex for vertex in distances if vertex not in visited),
        key=lambda vertex: distances[vertex])

    # Add the vertex to the set of visited vertices.
    visited.add(minimum_vertex)

    # For each edge connected to the vertex:
    for neighbor, weight in graph[minimum_vertex]:

      # If the distance to the neighbor is greater than the distance to the
      # vertex plus the weight of the edge:
      if distances[neighbor] > distances[minimum_vertex] + weight:

        # Update the distance to the neighbor.
        distances[neighbor] = distances[minimum_vertex] + weight

  return distances


# Get the graph from the user.
vertices = input("Enter the vertices: ").split()
edges = input("Enter the edges: ").split()

# Create a graph.
graph = {}
for vertex in vertices:
  graph[vertex] = []

# Add the edges to the graph.
for edge in edges:
  graph[edge[0]].append((edge[1], int(edge[2])))

# Get the source vertex from the user.
source = input("Enter the source vertex: ")

# Find the shortest paths from the source vertex to all other vertices.
distances = dijkstra(graph, source)

# Print the shortest paths.
for vertex, distance in distances.items():
  print(f"The distance from {source} to {vertex} is {distance}")