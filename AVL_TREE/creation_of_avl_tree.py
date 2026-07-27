#AVL Tree is the bst balanced tree
#If the bst is not balanced then we can do the rotation process to make it more balanced

class AVlNode:
    def __int__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

newAVL = AVlNode(3) #Only one node
#Time_complexity->o(1)
#Space-complexity->o(1)

