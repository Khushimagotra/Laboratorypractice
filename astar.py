import heapq
from typing import List

class Node:
    def __init__(self, name: str, hScore: int):
        self.name = name
        self.adjacencies = []
        self.hScore = hScore
        self.gScore = float('inf')
        self.parent = None

    def fScore(self):
        return self.gScore + self.hScore

    def __lt__(self, other):
        return self.fScore() < other.fScore()


class Edge:
    def __init__(self, end: Node, cost: int):
        self.end = end
        self.cost = cost

def printPath(target: Node) -> List[Node]:
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = node.parent
    path.reverse()
    return path

def AstarSearch(start: Node, goal: Node):
    explored = set()
    queue = []
    heapq.heapify(queue)
    start.gScore = 0
    heapq.heappush(queue, (start.fScore(), start))
    found = False
    
    while queue and not found:
        _, current = heapq.heappop(queue)
        explored.add(current)
        
        if current.name == goal.name:
            found = True
        
        for e in current.adjacencies:
            child = e.end
            cost = e.cost
            tempGScore = current.gScore + cost
            tempFScore = tempGScore + child.hScore
            
            if child in explored and tempFScore >= child.fScore():
                continue
            elif (child not in queue) or (tempFScore < child.fScore()):
                child.parent = current
                child.gScore = tempGScore
                
                if child in queue:
                    queue.remove(child)
                
                heapq.heappush(queue, (child.fScore(), child))

def main():
    nodes = []
    
    n = int(input("Enter the number of nodes in the graph: "))
    
    for i in range(n):
        name = input("Enter the name of node {}: ".format(i + 1))
        hScore = int(input("Enter the heuristic score of node {}: ".format(i + 1)))
        nodes.append(Node(name, hScore))
    
    for node in nodes:
        e = int(input("Enter the number of edges for node {}: ".format(node.name)))
        node.adjacencies = []
        
        for _ in range(e):
            endNode = input("Enter the name of the node that {} is connected to: ".format(node.name))
            cost = int(input("Enter the cost of the edge between {} and {}: ".format(node.name, endNode)))
            
            for n in nodes:
                if n.name == endNode:
                    end = n
                    break
            
            node.adjacencies.append(Edge(end, cost))
    
    startNode = input("Enter the name of the starting node: ")
    targetNode = input("Enter the name of the target node: ")
    
    start = None
    target = None
    
    for node in nodes:
        if node.name == startNode:
            start = node
        if node.name == targetNode:
            target = node
        if start and target:
            break
    
    AstarSearch(start, target)
    path = printPath(target)
    print("Path:", [node.name for node in path])

main()
