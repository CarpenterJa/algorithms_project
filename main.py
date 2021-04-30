from collections import defaultdict
from Graph import Graph
from FloydWarshallTraversial import FloydWarshallTraverisal


def ConfigGroceryStore(fileName):
    # Read in the config file
    # Generate the grocery store from the file

    # Try to open the file
    with open(fileName) as f:
        # Read until we hit no white space
        endOfFile = False
        while not endOfFile:
            newLine = f.readline()
            if len(newLine) == 0:
                endOfFile = True
            elif newLine[0:2] == "//":
                # Line is a comment so skip it
                continue
            elif len(newLine) > 0 and newLine == '\n':
                # Line is blank so skip it
                continue
            else:
                # Line is real text so decode it
                # The line contains escape a new line char so remove it
                newLine = newLine.replace('\n','')
                print(newLine)
                if newLine[0] == 'V':
                    # This line has the vertex number in it
                    # This will throw an error if  there is more than just a number on this line
                    vertexNum = int(newLine[1:])
                elif "Type:" in newLine:
                    # This line contains the category of food
                    foodType = ExtractVertexType("Type:",newLine)
                elif "Food:" in newLine:
                    # This line contains the food at this node
                    listOfFoods = ExtractVertexFood("Food:",newLine)
                elif "Edges:" in newLine:
                    # This line contains all the edges for this node
                    vertexEdges = ExtractEdges("Edges:",newLine)
                else:
                    # Unknown line so throw an error
                    pass
                
def ExtractVertexType(configId,configText):
    # Remove Type: from the line
    return configText.replace(configId,'')

def ExtractVertexFood(configId,configText):
    # Remove the configId from the line
    listOfFoodsStr = configText.replace(configId,'')

    # Remove any spaces
    listOfFoodsStr = listOfFoodsStr.replace(' ','')

    # Check if the line is equal to "None" which means there are no
    # items at this node. Probably a register or entrance/exit
    if(listOfFoodsStr == "None"):
        return None
    else:
        # Split line into a list
        listOfFoods = listOfFoodsStr.split(',')
        return listOfFoods

def ExtractEdges(configId,configText):
    # Remove the configId from the line
    listOfEdgesStr = configText.replace(configId,'')

    # Remove any space
    listOfEdgesStr = listOfEdgesStr.replace(' ','')

    # Split line into array
    listOfEdges = listOfEdgesStr.split(',')

    # Take the list of each edge and weight and convert the items to number
    # Then create a list of those edges and weights
    listOfEdgesNum = list()
    for edge in listOfEdges:
        foundStart = False
        foundEnd = False
        foundEdge = False
        foundWeight = False
        tempEdgeWeightPair = list()
        numAsStr = ""
        while len(edge) > 0 and foundEnd == False:
            # Find the start character of '['
            if not foundStart and edge[0] == "[":
                foundStart = True
            elif foundStart and edge[0] == "]":
                # Found the end of the edge weight pair
                foundEnd = True
            elif foundStart:
                if edge[0].isdigit():
                    # This char is a digit so add it to the value to convert
                    numAsStr += edge[0]
                else:
                    # This char is not a digit so we should convert
                    if foundEdge:
                        # Convert the number and add it to the edge slot
                        tempEdgeWeightPair.append(int(numAsStr))
                        foundEdge = True
                        numAsStr = ''
                    elif foundWeight:
                        # Conver the number and add it to the weight slot
                        tempEdgeWeightPair.append(int(numAsStr))
                        foundWeight = True
                        numAsStr = ''
                    else:
                        #Error
                        pass
            # Remove the first char from the string after each iteration
            edge = edge[1:]

        # Once out of the loop we can assemble the edge weight pair into the overall list
        listOfEdgesNum.append(tempEdgeWeightPair)
        
    return listOfEdgesNum


#------------------------------------------------------------------------------        
# Only run code if main called this file
if __name__ == "__main__":
    ConfigGroceryStore("groceryStoreConfig.txt")

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


