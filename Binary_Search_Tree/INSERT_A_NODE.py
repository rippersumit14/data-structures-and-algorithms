#Insertion of the node in a bst
#If the root node is blank -> edge case
#BST has some nodes in it
#declaring the class
class BSTnode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    #Insert method
    #Check the value of the node whether it is greater than the root node or lesser than the root node
def insert_node(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTnode(value)
        else:
            insert_node(rootNode.leftChild, value) #If there is a left subtree then add it recursively
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTnode(value)
        else:
            insert_node(rootNode.rightChild, value) #If there is a right subtree then add it recursively


#Time complexity will be o(logN) -> Adds the function to the call stack o(n/2)
#Space complexity will be o(n) -> Adds the recursive method in the call stack memory n times



NewBST = BSTnode(None)
print(insert_node(NewBST, 70))
print(insert_node(NewBST, 76))
print(insert_node(NewBST, 90))




