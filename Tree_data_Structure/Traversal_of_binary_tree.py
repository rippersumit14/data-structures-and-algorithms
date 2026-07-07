# -----------------------------------------------------
# Binary Tree Traversals
# -----------------------------------------------------

from collections import deque


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


print("Level Order Traversal:")
levelOrderTraversal(NewBT)

# Time Complexity : O(n)
# Space Complexity : O(n)