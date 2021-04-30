from collections import defaultdict
from Graph import Graph
from FloydWarshallTraversial import FloydWarshallTraverisal

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

    #groceryList = [2,7, 9, 5, 12]
    groceryList = [2,3,8,11]
    FWTraversial = FloydWarshallTraverisal(g.getNumVerticies())

    # Find all the shortest pairs
    FWTraversial.findShortestPairs(g)

    # Print the shortest pairs in a table
    FWTraversial.printShortestPairs(g.getNumVerticies())

    FWTraversial.print_final_path(FWTraversial.nodePermutation(groceryList))


