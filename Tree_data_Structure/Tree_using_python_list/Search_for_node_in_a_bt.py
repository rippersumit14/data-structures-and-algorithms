#Search for a node in the binary tree

#declaring the bt class
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    #Adding the insert method
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The binary tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The node is inserted"
    #Time_complexity -> o(1)
    #Space_complexity -> o(1)

    #Searching a node in a Binary Tree
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"
    #Time-complexity -> o(n)
    #Space_complexity -> o(1)




newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")

print(newBT.searchNode("Hot"))

