""" File:  Graph.py
Author:  Susan Fox
Date: September 2020

Contains an weighted adjacency list class
"""



# ======================================================================

class Graph:
    """A graph contains vertices and edges, this particular one is a weighted,
    adjacency-list implementation"""

    def __init__(self, n, nodeData = None):
        """
        Takes in the number of vertices, and an optional list of data the same length,
        and constructs the adjacency list representation of the data. Node data might
        be labels for the nodes, but generally we will refer to nodes by their numbers
        0 through n-1, same order as the nodeData
        :param n: The number of vertices in the graph
        :param nodeData: An optional list of labels/data to attach to each vertex
        """
        self.numVerts = n
        if nodeData is None:
            self.nodeData = list(range(n))
            self.lastData = 0
        else:
            self.nodeData = nodeData
            self.lastNode = len(nodeData)

        self.adjList = []
        for i in range(n):
            self.adjList.append(list())


    # -----------------------------------------------------------------
    # First, some operations for adding vertex data and edges to the graph


    def addNodeData(self, nodeData):
        """
        Takes a new node  item, and adds it to the next available node.  If no node is available, then it
        raises an exception, otherwise it returns the index of the node to which this data was added
        :param nodeData: New node data to be added at the next empty slot
        :return: 
        """
        if self.lastNode == self.numVerts:
            # if no more available nodes, return an error code
            raise GraphFullException()
        else:
            self.nodeData[self.lastNode] = nodeData
            nodePos = self.lastNode
            self.lastNode += 1
            return nodePos


    def addEdge(self, node1, node2, weight):
        """
        Takes two node indices and adds an edge between them. This means adding to the lists for each vertex
        Because this is a weighted graph, we will add a tuple containing the node number and the weight
        :param node1: Node number (not node data) for first node of the edge
        :param node2: Node number (not node data) for second node of the edge
        :return:
        """
        if node1 < self.numVerts and node2 < self.numVerts:
            self.adjList[node1].append((node2, weight))
            self.adjList[node2].append((node1, weight))
            return True
        elif node1 >= self.numVerts:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node1)
        else:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node2)

    

    def removeEdge(self, node1, node2):
        """
        Takes two nodes and removes any edge between them.  It returns
        True if the edge was there and was removed, and False if no edge was there.
        :param node1: First node number of edge to be removed
        :param node2: Second node number of edge to be removed
        :return:
        """
        if node1 < self.numVerts and node2 < self.numVerts:
            lst1 = self.adjList[node1]
            lst2 = self.adjList[node2]
            for (n, w) in lst1:
                if node2 == n:
                    lst1.remove((n, w))
            for (n, w) in lst2:
                if node1 == n:
                    lst2.remove((n, w))
            return True
        elif node1 >= self.numVerts:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node1)
        else:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node2)



    # ---------------------------------------------------------
    # Next, accessors of different sorts

    def getSize(self):
        """
        Returns the number of nodes in the graph
        """
        return self.numVerts

    def getVertices(self):
        """
        Returns a range containing the node numbers for the graph
        """
        return range(self.numVerts)
    
    
    def getData(self, node):
        """
        Takes in a node number, and returns the data associated with
        the node, if any. If nothing else, it returns the node number.
        :param node: Node number to look up
        :return:
        """
        if node < self.numVerts:
            return self.nodeData[node]
        else:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node)

        
    def findNode(self, data):
        """
        Takes in a data item, and returns the node index that contains the data item, if it exists.
        Otherwise it raises an exception
        :param data: The data item to look for
        :return:
        """
        if data in self.nodeData:
            return self.nodeData.index(data)
        else:
            raise NoSuchNodeException(data)


    def getNeighbors(self, node):
        """
        Takes in a node index, and returns a list of the indices of the node's neighbors.
        Note that this is a list of tuples, each containing the index of the neighbor node,
        and then the weight between them.
        :param node:
        :return: A new list of tuples, each tuple contains node index and edge weight
        """
        if node < self.numVerts:
            lst = self.adjList[node]
            return lst[:]
        else:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node)


    def areNeighbors(self, node1, node2):
        """
        Takes in two node indices, and returns True if they are neighbors and False if they are not.
        :param node1: First node to check
        :param node2: Second node to check
        :return: Returns True/False depending on whether there is an edge between the nodes
        """
        if node1 < self.numVerts and node2 < self.numVerts:
            for (n, w) in self.adjList[node1]:
                if n == node2:
                    return True
            return False
        elif node1 >= self.numVerts:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node1)
        else:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node2)


    def getWeight(self, node1, node2):
        """
        Takes in two node indices, and returns the weight between them, or None if they are not neighbors.
        :param node1: First node of the edge
        :param node2: Second node of the edge
        :return: The weight between them, if there is an edge, or None otherwise
        """
        if node1 < self.numVerts and node2 < self.numVerts:
            for (n, w) in self.adjList[node1]:
                if n == node2:
                    return w
            return None
        elif node1 >= self.numVerts:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node1)
        else:
            raise NodeIndexOutOfRangeException(0, self.numVerts, node2)

    
# ======================================================================
class NodeIndexOutOfRangeException(Exception):
    """A special exception for catching when a node reference is invalid"""
    
    def __init__(self, low, high, actual):
        self.low = low
        self.high = high
        self.actual = actual

    def __str__(self):
        s1 = "Expected node index in range " + str(self.low)
        s2  = " to " + str(self.high)
        s3 = "  Actual value was " + str(self.actual)
        return s1 + s2 + s3


class GraphFullException(Exception):
    """A special exception for catching when a graph can add no more nodes--
    or node data"""
    
    def __str__(self):
        s = "No more node data may be added: all nodes are in use"
        return s


class NoSuchNodeException(Exception):
    """A special exception for catching when node data is input that
    doesn't match any node data in the graph"""
    
    def __init__(self, data):
        self.data = data

    def __str__(self):
        s = "Node data " + str(self.data) + " not assigned to any node in the graph"
        return s
