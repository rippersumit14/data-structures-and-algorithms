#Searching a node in a BT
#Using level-Order_Traversal, because all other traversal use stack for the recursion calls but Level order-Traversal uses the Queue
import queue
# -----------------------------------------------------
# Binary Tree Traversals
# -----------------------------------------------------

from collections import deque

from Tree_data_Structure.Creation_of_basic_tree_in_python import cold


# -----------------------------------------------------
# Creating a Binary Tree Node
# -----------------------------------------------------

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# -----------------------------------------------------
# Creating the Binary Tree
# -----------------------------------------------------

# Root Node
NewBT = TreeNode("Drinks")

# Child Nodes
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

# Connecting Children
NewBT.leftChild = leftChild
NewBT.rightChild = rightChild


# -----------------------------------------------------
# Preorder Traversal
# Root -> Left -> Right
# -----------------------------------------------------

def preOrderTraversal(rootNode):

    # Base Case
    if rootNode is None:
        return

    # Visit Root
    print(rootNode.data)

    # Visit Left Subtree
    preOrderTraversal(rootNode.leftChild)

    # Visit Right Subtree
    preOrderTraversal(rootNode.rightChild)


print("Preorder Traversal:")
preOrderTraversal(NewBT)

# Time Complexity : O(n)
# Space Complexity : O(h)
# Worst Case : O(n)
# Balanced Tree : O(log n)

print()


# -----------------------------------------------------
# Inorder Traversal
# Left -> Root -> Right
# -----------------------------------------------------

def inOrderTraversal(rootNode):

    # Base Case
    if rootNode is None:
        return

    # Visit Left Subtree
    inOrderTraversal(rootNode.leftChild)

    # Visit Root
    print(rootNode.data)

    # Visit Right Subtree
    inOrderTraversal(rootNode.rightChild)


print("Inorder Traversal:")
inOrderTraversal(NewBT)

# Time Complexity : O(n)
# Space Complexity : O(h)

print()


# -----------------------------------------------------
# Postorder Traversal
# Left -> Right -> Root
# -----------------------------------------------------

def postOrderTraversal(rootNode):

    # Base Case
    if rootNode is None:
        return

    # Visit Left Subtree
    postOrderTraversal(rootNode.leftChild)

    # Visit Right Subtree
    postOrderTraversal(rootNode.rightChild)

    # Visit Root
    print(rootNode.data)


print("Postorder Traversal:")
postOrderTraversal(NewBT)

# Time Complexity : O(n)
# Space Complexity : O(h)

print()


# -----------------------------------------------------
# Level Order Traversal (Breadth First Search)
# Level by Level using Queue
# -----------------------------------------------------

def levelOrderTraversal(rootNode):

    # Base Case
    if rootNode is None:
        return

    # Create Queue
    queue = deque()

    # Insert Root Node
    queue.append(rootNode)

    # Traverse until Queue becomes empty
    while queue:

        # Remove the front node
        currentNode = queue.popleft()

        # Visit the current node
        print(currentNode.data)

        # Insert Left Child into Queue
        if currentNode.leftChild is not None:
            queue.append(currentNode.leftChild)

        # Insert Right Child into Queue
        if currentNode.rightChild is not None:
            queue.append(currentNode.rightChild)


# -----------------------------------------------------
# Search a Node in Binary Tree using Level Order Traversal
# -----------------------------------------------------

def searchBT(rootNode, nodeValue):

    # Base Case
    if rootNode is None:
        return "The Binary Tree does not exist."

    # Create Queue
    customQueue = deque()

    # Insert Root Node
    customQueue.append(rootNode)

    # Traverse the tree level by level
    while customQueue:

        # Remove front node
        currentNode = customQueue.popleft()

        # Check if current node contains the value
        if currentNode.data == nodeValue:
            return "Success! Node Found."

        # Insert Left Child
        if currentNode.leftChild is not None:
            customQueue.append(currentNode.leftChild)

        # Insert Right Child
        if currentNode.rightChild is not None:
            customQueue.append(currentNode.rightChild)

    # Node not found
    return "Node Not Found."

print(searchBT(NewBT, "cold"))
#Time-complexity -> o(n)
#Space-complexity -> o(n) -> Creating a custom queue

print("Level Order Traversal:")
levelOrderTraversal(NewBT)

# Time Complexity : O(n)
# Space Complexity : O(n)


#Insert a node in a bt
#To insert a node in a bt
#A root is blank
#The tree exists , we have to look for a first vacant place
#Whichever vacant place will come first in the Level order Traversal We will take that

# -----------------------------------------------------
# Insert a Node into Binary Tree
# Level Order Traversal (BFS)
# -----------------------------------------------------

def insertNodeBt(rootNode, newNode):

    # If Tree is Empty
    if rootNode is None:
        rootNode = newNode
        return "Successfully Inserted"

    # Create Queue
    customQueue = deque()

    # Insert Root
    customQueue.append(rootNode)

    while customQueue:

        # Remove Front Node
        currentNode = customQueue.popleft()

        # Check Left Child
        if currentNode.leftChild is not None:
            customQueue.append(currentNode.leftChild)

        else:
            currentNode.leftChild = newNode
            return "Successfully Inserted"

        # Check Right Child
        if currentNode.rightChild is not None:
            customQueue.append(currentNode.rightChild)

        else:
            currentNode.rightChild = newNode
            return "Successfully Inserted"

newNode = TreeNode("Guns")
insertNodeBt(NewBT, newNode)
levelOrderTraversal(NewBT)













