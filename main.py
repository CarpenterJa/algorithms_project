from collections import defaultdict
from Graph import Graph
from FloydWarshallTraversial import FloydWarshallTraverisal
from GroceryStore import GroceryStore
import re

debug = False




#------------------------------------------------------------------------------        
# Only run code if main called this file
if __name__ == "__main__":
    groceryStore = GroceryStore("groceryStoreConfig.txt")
    groceryList = [2,3,8,11]
    FWTraversial = FloydWarshallTraverisal(groceryStore.getGroceryStoreGraph().getNumVerticies())

    # Find all the shortest pairs
    FWTraversial.findShortestPairs(groceryStore.getGroceryStoreGraph())

    # Print the shortest pairs in a table
    #FWTraversial.printShortestPairs(testG.getNumVerticies())

    # Print the path for the config graph
    print("The grocery list is:")
    print(groceryList)

    print("\nThe optimal path for the grocery list is:")
    FWTraversial.print_final_path(FWTraversial.nodePermutation(groceryList),debugEnabled=debug)