from collections import defaultdict
import math
from enum import Enum
from itertools import permutations

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
 
class FloydWarshallTraverisal():
    #https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    distances = None
    nextVert = None
    normPrintWidth = 7
    newLinePrintWidth = 3

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
        print("Matrix shows the distance from each node to another")
        print("*INF means no path between those nodes*\n")

        # Print matrix header of vertex number
        for i in range(numVerticies):
            if i == 0:
                print("{0: >{width}}".format(i,width = (self.normPrintWidth + self.newLinePrintWidth-1)),end='') 
            else:
                print("{0: >{width}}".format(i,width = self.normPrintWidth),end='') 

        # Draw line across top
        print("\n"+ "-"* (self.newLinePrintWidth-1) + "-"*self.normPrintWidth * numVerticies)

        tempSpacing = self.normPrintWidth
        for i in range(numVerticies):
            # Draw vertical line at each new line
            print("{0: >3} | ".format(i),end="")
            firstOnLine = True
            for j in range(numVerticies):
                if firstOnLine:
                    # Do a different print line to fix spacing
                    tempSpacing = self.newLinePrintWidth
                    firstOnLine = False
                else:
                    tempSpacing = self.normPrintWidth

                if(self.distances[i][j] == math.inf):
                    # Print without new line
                    print("{0: >{width}}".format("INF", width = tempSpacing),end='')
                else:
                    print("{0: >{width}}".format(self.distances[i][j], width = tempSpacing),end='')
            print("")       

    def getPathFor(self, startVert, endVert):
        if self.nextVert[startVert][endVert] == None:
            return None
        
        path = [startVert]
        nextVert = startVert
        while not(nextVert == endVert):
            nextVert = self.nextVert[nextVert][endVert]
            path.append(nextVert)

        return path

    def nodePermutation(self, mustPassNodesList):
        list_of_permutations = list(permutations(mustPassNodesList))
        list_of_permutations = [list(ele) for ele in list_of_permutations]
        total_distance = 0
        min_distance = math.inf
        print("Distances of Paths:")
        for p in list_of_permutations:
            p.insert(0,0)
            p.append(13)
            for index, elem in enumerate(p):
                if (index + 1 < len(p)):
                    next_el = p[index + 1]
                    total_distance += self.get_distance_between_verticies(elem, next_el)
            if(total_distance < min_distance):
                min_distance = total_distance
                optimal_path = p
            print(str(total_distance))
            total_distance = 0
        print("List of Permutations:")
        print(list_of_permutations)
        print("Min Distance: \n" + str(min_distance))
        print("Optimal Path:")
        print(optimal_path)
        return optimal_path

    def print_final_path(self, must_past_list):
        total_path = []
        for index, elem in enumerate(must_past_list):
            if (index + 1 < len(must_past_list)):
                next_el = must_past_list[index + 1]
                total_path.append(self.getPathFor(elem, next_el))
        print(total_path)
        #for vertex in total_path:
            #print(vertex)

    def get_distance_between_verticies(self, vertex, link):
        return self.distances[vertex][link]

    # def getLengthOfPath(self, startVert, endVert):
    #     # Get path
    #     path = self.getPathFor(startVert,endVert)
    #     if not(path == None):
    #         totalDist = 0
    #         for step in path:
    #             totalDist = totalDist + 



#------------------------------------------------------------------------------        
# Only run code if main called this file
if __name__ == "__main__":
    totalNodes = 14
    g = Graph(totalNodes)

    # Starting node
    g.addEdge(0, 1, 20)
    g.addEdge(1, 0, 20)

    # Add links for node 1
    g.addEdge(1, 13, 15)
    g.addEdge(1, 2, 15)
    g.addEdge(1, 5, 10)
    g.addEdge(13, 1, 15)
    g.addEdge(2, 1, 15)
    g.addEdge(5, 1, 10)

    # Add links for node 2
    g.addEdge(2, 6, 10)
    g.addEdge(2, 3, 15)
    g.addEdge(6, 2, 10)
    g.addEdge(3, 2, 15)

    # Add links for node 3
    g.addEdge(3, 4, 15)
    g.addEdge(3, 7, 10)
    g.addEdge(4, 3, 15)
    g.addEdge(7, 3, 10)

    # Add links for node 4
    g.addEdge(4, 8, 10)
    g.addEdge(8, 4, 10)

    # Add links for node 5
    g.addEdge(5, 9, 10)
    g.addEdge(9, 5, 10)

    # Add links for node 6
    g.addEdge(6, 10, 10)
    g.addEdge(10, 6, 10)

    # Add links for node 7
    g.addEdge(7, 11, 10)
    g.addEdge(11, 7, 10)

    # Add links for node 8
    g.addEdge(8, 12, 10)
    g.addEdge(12, 8, 10)

    # Add links for node 9
    g.addEdge(9, 13, 20)
    g.addEdge(9, 10, 15)
    g.addEdge(13, 9, 20)
    g.addEdge(10, 9, 15)

    # Add links for node 10
    g.addEdge(10, 11, 15)
    g.addEdge(11, 10, 15)

    # Add links for node 11
    g.addEdge(11, 12, 15)
    g.addEdge(12, 11, 15)

    groceryList = [9, 5, 12]
    FWTraversial = FloydWarshallTraverisal(g.getNumVerticies())

    # Find all the shortest pairs
    FWTraversial.findShortestPairs(g)

    # Find the shortest path given a starting index
    FWTraversial.findShortestPath(g.getNumVerticies())

    # Print shortest path between node 1 and 10
    #path = FWTraversial.getPathFor(0, 9)

    #for vertex in path:
        #print(vertex)

    print(FWTraversial.get_distance_between_verticies(6, 12))
    FWTraversial.print_final_path(FWTraversial.nodePermutation(groceryList))


