from collections import defaultdict
import math
from enum import Enum
# Class to represent a graph
 
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
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):
 
        result = []  # This will store the resultant MST
         
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
 
class FloydWarshallTraverisal():
    distances = None
    nextVert = None

    def __init__(self, numVerticies):
        #numVerticies = numVerticies - 1

        # https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
        # Make array to hold all the minimum distances
        # Make single array with numVerticies indices
        self.distances = list(range(numVerticies))
        for i in range(numVerticies):
            # Each index holds another array making it a 2d array
            self.distances[i] = list(range(numVerticies))
            for q in range(numVerticies):
                self.distances[i][q] = math.inf

        # Make array to hold vertex indicies
        self.nextVert = list(range(numVerticies))
        for i in range(numVerticies):
            self.nextVert[i] = list(range(numVerticies))
            for q in range(numVerticies):
                self.nextVert[i][q] = None

    def findShortestPairs(self, graph):
        print(Graph.GraphEnums.VERTEX.value)
        for edge in graph.graph:
            u = edge[Graph.GraphEnums.VERTEX.value]
            v = edge[Graph.GraphEnums.LINK.value]
            self.distances[u][v] = edge[Graph.GraphEnums.WEIGHT.value]
            self.nextVert[u][v] = v

        for vertex in range(graph.V):
            self.distances[vertex][vertex] = 0
            self.nextVert[vertex][vertex] = vertex

        for k in range(graph.V):
            for i in range(graph.V):
                for j in range(graph.V):
                    distSum = (self.distances[i][k] + self.distances[k][j])
                    if self.distances[i][j] > distSum:
                        self.distances[i][j] = distSum
                        self.nextVert[i][j] = self.nextVert[i][k]
    
    def findShortestPath(self, numVerticies):
        print("Following matrix shows the shortest distances between every pair of vertices")
        for i in range(numVerticies):
            for j in range(numVerticies):
                if(self.distances[i][j] == math.inf):
                    # Print without new line
                    print("{0: >7}".format("INF"),end='')
                    #print("%5s" % ("INF"),end='')
                else:
                    print("{0: >7}".format(self.distances[i][j]),end='')
                    #print("%4d" % (self.distances[i][j]), end='')
            print("")       
        
        # u = edge[Graph.GraphEnums.VERTEX]
        # v = edge[Graph.GraphEnums.LINK]
        # if self.nextVert[u][v] == None:
        #     return None
        
        # path = [u]
        # while not(u == v):
        #     u = self.nextVert[u][v]
        #     path.append(u)
        # return path

#------------------------------------------------------------------------------        
# Only run code if main called this file
if __name__ == "__main__":
    totalNodes = 14
    g = Graph(totalNodes)

    # Starting node
    g.addEdge(0,1,20)

    # Add links for node 1
    g.addEdge(1,13,15)
    g.addEdge(1,2,15)
    g.addEdge(1,5,10)

    # Add links for node 2
    g.addEdge(2,6,10)
    g.addEdge(2,3,15)

    # Add links for node 3
    g.addEdge(3,4,15)
    g.addEdge(3,7,10)

    # Add links for node 4
    g.addEdge(4,8,10)

    # Add links for node 5
    g.addEdge(5,9,10)

    # Add links for node 6
    g.addEdge(6,10,10)

    # Add links for node 7
    g.addEdge(7,11,10)

    # Add links for node 8
    g.addEdge(8,12, 10)

    # Add links for node 9
    g.addEdge(9,13,20)
    g.addEdge(9,10,15)

    # Add links for node 10
    g.addEdge(10,11,15)

    # Add links for node 11
    g.addEdge(11,12,15)

    FWTraversial = FloydWarshallTraverisal(g.getNumVerticies())

    # Find all the shortest pairs
    FWTraversial.findShortestPairs(g)

    # Find the shortest path given a starting index
    FWTraversial.findShortestPath(g.getNumVerticies())
