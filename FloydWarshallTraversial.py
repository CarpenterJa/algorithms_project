from Graph import Graph
import math
from itertools import permutations

class FloydWarshallTraverisal():
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
    
    def printShortestPairs(self, numVerticies, debugEnabled = False):
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

    def nodePermutation(self, mustPassNodesList,startVertex, endVertex, debugEnabled = False):
        list_of_permutations = list(permutations(mustPassNodesList))
        list_of_permutations = [list(ele) for ele in list_of_permutations]
        total_distance = 0
        min_distance = math.inf

        if debugEnabled:
            print("Distances of Paths:")

        for p in list_of_permutations:
            p.insert(0,startVertex)
            p.append(endVertex)
            for index, elem in enumerate(p):
                if (index + 1 < len(p)):
                    next_el = p[index + 1]
                    total_distance += self.get_distance_between_verticies(elem, next_el)
            if(total_distance < min_distance):
                min_distance = total_distance
                optimal_path = p

            if debugEnabled:
                print(str(total_distance))

            total_distance = 0
        
        if debugEnabled:
            print("List of Permutations:")
            print(list_of_permutations)
            print("Min Distance: \n" + str(min_distance))
            print("Optimal Permutation of Required Nodes:")
            print(optimal_path)
        return optimal_path

    def print_final_path(self, must_past_list):
        total_path = []

        print("Full Path:")

        for index, elem in enumerate(must_past_list):
            if (index + 1 < len(must_past_list)):
                next_el = must_past_list[index + 1]
                total_path.append(self.getPathFor(elem, next_el))

        print(total_path)

        # Take final path and remove nodes that are repeated
        # example list [[0, 1], [1, 2], [2, 3, 4]]
        # the real path would be [0, 1, 2, 3, 4]
        # because we are already at node 1 so we don't need to repeat it in the next path
        totalPathFixed = list()
        if len(total_path) > 1:
            for vertex in total_path[0]:
                totalPathFixed.append(vertex)

            for i in range(1,len(total_path)):
                for vertex in total_path[i][1:]:
                    totalPathFixed.append(vertex)

            print(totalPathFixed)

    def get_distance_between_verticies(self, vertex, link):
        return self.distances[vertex][link]