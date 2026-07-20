#Insert a node in Binary Tree
#Declaring the bt class
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size


    #Insert method
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The bt is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value is successfully inserted"

    #Time-complexity => o(1)
    #Space-complexity => o(1)









newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")

