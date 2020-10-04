"""
This contains some sample code showing how to work with my Graph class
"""

from Graph import Graph



g1 = Graph(5, ['A', 'B', 'C', 'D', 'E'])

g1.addEdge(0, 1, 25)    # Edge from A to B
g1.addEdge(0, 2, 12)    # Edge from A to C
g1.addEdge(1, 3, 16)    # Edge from B to D
g1.addEdge(1, 4, 22)    # Edge from B to E
g1.addEdge(2, 4, 31)    # Edge from C to E
g1.addEdge(2, 3, 10)    # Edge from C to D


print(g1.adjList)

print("A's neighbors:", g1.getNeighbors(0))
print("Are A and C adjacent?", g1.areNeighbors(0, 2))
print("Weight between C and E:", g1.getWeight(2, 4))
print("Size:", g1.getSize())
print("GetData:", g1.getData(4))
print("Index for B:", g1.findNode('B'))
print("Vertices:", g1.getVertices())

g1.removeEdge(1, 4)
print("Are B and E neighbors?", g1.areNeighbors(1, 4))
print(g1.adjList)


