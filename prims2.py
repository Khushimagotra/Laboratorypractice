import random


def prims(graph):
  """
  This function implements Prim's minimum spanning tree algorithm.

  Args:
    graph: A graph represented as a list of lists. Each inner list represents
      the edges connected to a vertex.

  Returns:
    A list of edges that form the minimum spanning tree.
  """

  # Initialize the minimum spanning tree.
  mst = []

  # Initialize the set of visited vertices.
  visited = set()

  # Start with a random vertex.
  current_vertex = random.choice(list(graph.keys()))

  # While there are still vertices to visit:
  while len(visited) < len(graph):

    # Find the edge with the minimum weight that connects a visited vertex to
    # an unvisited vertex.
    minimum_edge = min(
        (edge for edge in graph[current_vertex] if edge[0] not in visited),
        key=lambda edge: edge[1])

    # Add the edge to the minimum spanning tree.
    mst.append(minimum_edge)

    # Add the vertex to the set of visited vertices.
    visited.add(minimum_edge[0])

    # Set the current vertex to the vertex at the other end of the edge.
    current_vertex = minimum_edge[1]

  return mst


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

# Find the minimum spanning tree.
mst = prims(graph)

# Print the minimum spanning tree.
print("The minimum spanning tree is:")
for edge in mst:
  print(edge)