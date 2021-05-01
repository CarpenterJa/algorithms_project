from collections import defaultdict
from Graph import Graph
from FloydWarshallTraversial import FloydWarshallTraverisal

from GroceryStore import GroceryStore
import re

debug = False

def CreateGroceryList(file_name):
    grocery_list = list()
    with open(file_name) as f:
        eof = False
        while not eof:
            new_line = f.readline()
            if len(new_line) == 0:
                eof = True
            elif new_line[0:2] == "//":
                continue
            elif len(new_line) > 0 and new_line == '\n':
                continue
            else:
                new_line = new_line.replace("\n", "")
                grocery_list.append(new_line)
    return grocery_list

def findNodes (store_array, grocery_list):
    vertex_array = list()
    for i in range(len(store_array)):
        for j in range(len(store_array[i])):
            for k in range(len(grocery_list)):
                if store_array[i][j] == grocery_list[k]:
                    vertex_array.append(i) # return the row representing the vertex / node
    return vertex_array

#------------------------------------------------------------------------------
# Only run code if main called this file
if __name__ == "__main__":
    groceryStore = GroceryStore("groceryStoreConfig.txt")

    groceryList = CreateGroceryList("groceryList.txt")
    groceryListVertices = findNodes(groceryStore.getGroceryStoreFoods(), groceryList)

    groceryList2 = [2,3,8,11]
    FWTraversial = FloydWarshallTraverisal(groceryStore.getGroceryStoreGraph().getNumVerticies())

    # Find all the shortest pairs
    FWTraversial.findShortestPairs(groceryStore.getGroceryStoreGraph())

    # Print the path for the config graph
    print("The grocery list is:")
    print(groceryList)

    print("\nThe optimal path for the grocery list is:")
    FWTraversial.print_final_path(FWTraversial.nodePermutation(groceryListVertices),debugEnabled=debug)