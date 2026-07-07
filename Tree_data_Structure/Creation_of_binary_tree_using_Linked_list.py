#creation of binary tree using linked list

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")

#Time-complexity->o(1)
#Space-complexity->o(1)

#traversal is used heavily for the insertion of a node in the binary tree
