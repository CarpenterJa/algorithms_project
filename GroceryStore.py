from Graph import Graph
import re

class GroceryStore:
    groceryStoreGraph = None
    groceryStoreFoods = None

    def __init__(self, configFilePath):
        if configFilePath == None:
            raise filename

        self.groceryStoreFoods = list()

        self.groceryStoreGraph,self.groceryStoreFoods = self.ConfigGroceryStore(configFilePath)

    def ConfigGroceryStore(self,fileName,debug = False):
        # Read in the config file
        # Generate the grocery store from the file

        g = None
        numVerticies = 0
        vertexFoodList = list()

        # Try to open the file
        with open(fileName) as f:
            # Read until we hit no white space
            endOfFile = False
            infoReadIn = 0
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
                    if debug:
                        print(newLine)

                    if "NumVertex" in newLine:
                        newLine = newLine.replace("NumVertex:","",1)
                        numVerticies = int(newLine)
                        output = self.InitVars(numVerticies)

                        g = output[0] 
                        vertexFoodList = output[1]

                    elif newLine[0] == 'V':
                        # This line has the vertex number in it
                        # This will throw an error if  there is more than just a number on this line
                        vertexNum = int(newLine[1:])
                        infoReadIn += 1
                    elif "Type:" in newLine:
                        # This line contains the category of food
                        foodType = self.ExtractVertexType("Type:",newLine)
                        infoReadIn += 1
                    elif "Food:" in newLine:
                        # This line contains the food at this node
                        listOfFoods = self.ExtractVertexFood("Food:",newLine)
                        infoReadIn += 1
                    elif "Edges:" in newLine:
                        # This line contains all the edges for this node
                        vertexEdges = self.ExtractEdges("Edges:",newLine)
                        infoReadIn += 1
                    else:
                        # Unknown line so throw an error
                        pass

                # If we read in all the information then add the node to our data structures
                if infoReadIn == 4:
                    # Add all the edges
                    for edge in vertexEdges:
                        g.addEdge(vertexNum,edge[0],edge[1])

                    # Add all the food items from this node
                    for food in listOfFoods:
                        vertexFoodList[vertexNum].append(food)
                    infoReadIn = 0

        return (g,vertexFoodList)

    def InitVars(self, numVerticies):
        graph = Graph(numVerticies)

        foodList = list()
        for _ in range(numVerticies):
            foodList.append(list())

        return (graph,foodList)
                    
    def ExtractVertexType(self,configId,configText):
        # Remove Type: from the line
        return configText.replace(configId,'')

    def ExtractVertexFood(self,configId,configText):
        # Remove the configId from the line
        listOfFoodsStr = configText.replace(configId,'')

        # Remove any spaces
        listOfFoodsStr = listOfFoodsStr.replace(' ','')

        # Check if the line is equal to "None" which means there are no
        # items at this node. Probably a register or entrance/exit
        if(listOfFoodsStr == "None"):
            return ["None"]
        else:
            # Split line into a list
            listOfFoods = listOfFoodsStr.split(',')
            return listOfFoods

    def ExtractEdges(self,configId,configText):
        # Remove the configId from the line
        listOfEdgesStr = configText.replace(configId,'')

        # Remove any space
        listOfEdgesStr = listOfEdgesStr.replace(' ','')

        # Split line into array
        #listOfEdges = listOfEdgesStr.split('[')
        # https://www.geeksforgeeks.org/python-extract-substrings-between-brackets/
        listOfEdges = re.findall(r'\[.*?\]', listOfEdgesStr)

        # Take the list of each edge and weight and convert the items to number
        # Then create a list of those edges and weights
        listOfEdgesNum = list()
        for edge in listOfEdges:
            foundStart = False
            foundEnd = False
            foundEdge = False
            tempEdgeWeightPair = list()
            numAsStr = ""
            while len(edge) > 0 and foundEnd == False:
                # Find the start character of '['
                if not foundStart and edge[0] == "[":
                    foundStart = True
                elif foundStart and edge[0] == "]":
                    # Found the end of the edge weight pair
                    foundEnd = True

                    # Convert the final number if there are digits
                    if len(numAsStr) > 0:
                        # Conver the number and add it to the weight slot
                        tempEdgeWeightPair.append(int(numAsStr))
                elif foundStart:
                    if edge[0].isdigit():
                        # This char is a digit so add it to the value to convert
                        numAsStr += edge[0]
                    else:
                        # This char is not a digit so we should convert
                        if not foundEdge:
                            # Convert the number and add it to the edge slot
                            tempEdgeWeightPair.append(int(numAsStr))
                            foundEdge = True
                            numAsStr = ''
                        else:
                            #Error
                            pass

                # Remove the first char from the string after each iteration
                edge = edge[1:]

            # Once out of the loop we can assemble the edge weight pair into the overall list
            listOfEdgesNum.append(tempEdgeWeightPair)
            
        return listOfEdgesNum

    def getGroceryStoreGraph(self):
        return self.groceryStoreGraph
        
    def getGroceryStoreFoods(self):
        return self.groceryStoreFoods