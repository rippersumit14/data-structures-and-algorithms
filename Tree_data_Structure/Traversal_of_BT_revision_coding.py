#Revising the traversal of the bt

from collections import deque

#Creating a binary tree node
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


#Creating a binary tree
NewBt = TreeNode("Drinks")

#Child Nodes
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

#connectiong children
NewBt.leftChild = leftChild
NewBt.rightChild = rightChild

#Pre-Order Traversal-> Root->Left->Right
def preOrderTraversal(rootNode):
    #Base case
    if not rootNode:
        return
    print(rootNode)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(NewBt)
#Time - complexity -> o(n)
#Space - complexity -> o(n)

#In-order Traversal -> Left -> Root -> Right
def InOrder(rootNode):
    #Base case
    if not rootNode:
        return
    InOrder(rootNode.leftChild)
    print(rootNode)
    InOrder(rootNode.rightChild)

InOrder(NewBt)
#Time-complexity-> o(n)
#Space-complexity-> o(n)

#Post-Order Traversal -> left-> right -> Root
def post_order(rootNode):
    #Base case
    if rootNode:
        return
    post_order(rootNode.leftChild)
    post_order(rootNode.rightChild)
    print(rootNode)
post_order(NewBt)

#Level order Traversal(BFS)-> Nodes are visited level by level starting from the root
def levelOrderTraversal(rootNode):
    #Base case
    if rootNode is None:
        return

    #Create a queue
    queue = deque()

    #Insert Root Node
    queue.append(rootNode)

    #Traverse until Queue becomes empty
    while queue:
        current_node = queue.popleft()

        print(current_node.data)

        if current_node.leftChild is not None:
            queue.append(current_node.leftChild)

        if current_node.rightChild is not None:
            queue.append(current_node.rightChild)


levelOrderTraversal(NewBt)
#Time-complexity -> o(n)
#Space-complexity -> o(n)
