def graph_coloring(graph, colors):
    def is_safe(node, color, assignment):
        # Check if it's safe to assign the given color to the node
        for neighbor in graph[node]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(node):
        # Base case: All nodes are assigned colors
        if node == len(graph):
            return True

        for color in colors:
            if is_safe(list(graph.keys())[node], color, assignment):
                assignment[list(graph.keys())[node]] = color
                if backtrack(node + 1):
                    return True
                del assignment[list(graph.keys())[node]]  # Backtrack and remove the color assignment
        return False

    assignment = {}  # Dictionary to store color assignments for each node

    if backtrack(0):
        return assignment
    else:
        return None

# Example usage:
graph = {}
n = int(input("Enter the number of nodes: "))
for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")
    neighbors = input(f"Enter the neighbors of node {node} (space-separated): ").split()
    graph[node] = neighbors

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']  # List of colors

solution = graph_coloring(graph, colors)

if solution:
    print("Solution found:")
    for node, color in solution.items():
        print(f"Node {node} -> Color: {color}")
else:
    print("No solution found.")