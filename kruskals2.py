import sys

def kruskal(vertices, edges):
  """
  Kruskal's algorithm to find the minimum spanning tree of a graph.

  Args:
    vertices: A list of vertices in the graph.
    edges: A list of edges in the graph.

  Returns:
    A list of edges in the minimum spanning tree.
  """

  # Sort the edges by weight.
  edges.sort(key=lambda e: e[2])

  # Create a union-find data structure to track which vertices are connected.
  uf = UnionFind(vertices)

  # Add edges to the minimum spanning tree until all vertices are connected.
  mst = []
  for edge in edges:
    if not uf.is_connected(edge[0], edge[1]):
      mst.append(edge)
      uf.union(edge[0], edge[1])

  return mst


class UnionFind:
  """
  A union-find data structure.

  This data structure tracks which elements are connected and allows us to
  efficiently find the union of two elements.
  """

  def __init__(self, elements):
    """
    Initialize the union-find data structure.

    Args:
      elements: A list of elements to track.
    """

    self.parent = list(range(len(elements)))
    self.rank = [1] * len(elements)

  def find(self, x):
    """
    Find the representative of the set that x belongs to.

    Args:
      x: An element.

    Returns:
      The representative of the set that x belongs to.
    """

    while x != self.parent[x]:
      x = self.parent[x]
    return x

  def union(self, x, y):
    """
    Combine the sets that x and y belong to.

    Args:
      x: An element.
      y: An element.
    """

    x_root = self.find(x)
    y_root = self.find(y)

    if x_root == y_root:
      return

    if self.rank[x_root] < self.rank[y_root]:
      x, y = y, x

    self.parent[y_root] = x_root
    self.rank[x_root] += self.rank[y_root]

  def is_connected(self, x, y):
    """
    Return whether x and y belong to the same set.

    Args:
      x: An element.
      y: An element.

    Returns:
      True if x and y belong to the same set, False otherwise.
    """

    return self.find(x) == self.find(y)


def main():
  """
  Main function.

  This function prompts the user to enter the number of vertices and edges in a
  graph. It then uses Kruskal's algorithm to find the minimum spanning tree of
  the graph and prints the edges in the minimum spanning tree.
  """

  num_vertices = int(input("Enter the number of vertices: "))
  num_edges = int(input("Enter the number of edges: "))

  vertices = list(range(num_vertices))
  edges = []

  for _ in range(num_edges):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

  mst = kruskal(vertices, edges)

  print("The minimum spanning tree is:")
  for edge in mst:
    print(edge)


if __name__ == "__main__":
  main()