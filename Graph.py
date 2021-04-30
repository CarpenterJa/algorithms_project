from enum import Enum

# Graph class comes from https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
class Graph:
    class GraphEnums(Enum):
        VERTEX = 0
        LINK = 1
        WEIGHT = 2

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph
 
    # function to add an edge to graph
    def addEdge(self, rootNode, nodeToLink, weight):
        self.graph.append([rootNode, nodeToLink, weight])
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def getNumVerticies(self):
        return self.V

    def getEdgesForVertex(self, vertex):
        if(vertex > self.V):
            return None

        edges = []
        for edge in self.graph:
            # Check if the vertex of the edge is what we are looking for
            if edge[self.GraphEnums.VERTEX.value] == vertex or \
               edge[self.GraphEnums.LINK.value] == vertex:
                # Add thie edge to the list of edges
                edges.append(edge)

        return edges

    def getEdgeLength(self, vertex, link) :
        edges = self.getEdgesForVertex(vertex)

        # Possible options for each edge
        # [vertex,link,weight]
        # [link,vertex,weight]
        
        for edge in edges:
            if (edge[self.GraphEnums.VERTEX.value] == vertex and edge[self.GraphEnums.LINK.value] == link) or \
               (edge[self.GraphEnums.VERTEX.value] == link and edge[self.GraphEnums.LINK.value] == vertex):
                return edge[self.GraphEnums.WEIGHT.value]

        return -1
 