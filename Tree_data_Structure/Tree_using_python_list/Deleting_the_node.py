#Traversal through a bt using python list
#Defining the bt class
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    #Adding the insert method
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The BT is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "Node is inserted"

    #Search method
    def search(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Node found"
        return "Node not found"

    #Traversal Method
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])#rootNode
        self.preOrderTraversal(index*2)#left subtree
        self.preOrderTraversal(index*2 + 1)#Right subtree

    #Time complexity-> o(n)
    #Space complexity-> o(n)

    #Adding the inorder traversal method
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)#Left subtree
        print(self.customList[index])#Root node
        self.inOrderTraversal(index*2 + 1)#Right subtree

    #Time-complexity-> o(n)
    #Space-complexity-> o(n)

    #Adding the postOrder traversal method
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])

    #Time-Complexity->o(n)
    #Space-Complexity->o(n)

    #Deleting the node
    #Find the deepest node
    #Replace the value of the deepest node with the node that is to be deleted







newBt = BinaryTree(10)
newBt.insertNode("N1")
newBt.insertNode("N2")
newBt.insertNode("N3")
newBt.insertNode("N4")
newBt.insertNode("N5")
newBt.insertNode("N6")

print(newBt.preOrderTraversal(5))

