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

NewBT = TreeNode("Drinks")

leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

NewBT.leftChild = leftChild
NewBT.rightChild = rightChild


# -----------------------------------------------------
# Preorder Traversal
# Root -> Left -> Right
# Time Complexity : O(n)
# Space Complexity : O(h)
# -----------------------------------------------------

def preOrderTraversal(rootNode):
    if rootNode is None:
        return

    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# -----------------------------------------------------
# Inorder Traversal
# Left -> Root -> Right
# Time Complexity : O(n)
# Space Complexity : O(h)
# -----------------------------------------------------

def inOrderTraversal(rootNode):
    if rootNode is None:
        return

    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# -----------------------------------------------------
# Postorder Traversal
# Left -> Right -> Root
# Time Complexity : O(n)
# Space Complexity : O(h)
# -----------------------------------------------------

def postOrderTraversal(rootNode):
    if rootNode is None:
        return

    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# -----------------------------------------------------
# Level Order Traversal
# BFS using Queue
# Time Complexity : O(n)
# Space Complexity : O(n)
# -----------------------------------------------------

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return

    customQueue = deque()
    customQueue.append(rootNode)

    while customQueue:
        currentNode = customQueue.popleft()
        print(currentNode.data)

        if currentNode.leftChild is not None:
            customQueue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            customQueue.append(currentNode.rightChild)


# -----------------------------------------------------
# Search Node in Binary Tree
# Using Level Order Traversal
# Time Complexity : O(n)
# Space Complexity : O(n)
# -----------------------------------------------------

def searchBT(rootNode, nodeValue):
    if rootNode is None:
        return "The Binary Tree does not exist."

    customQueue = deque()
    customQueue.append(rootNode)

    while customQueue:
        currentNode = customQueue.popleft()

        if currentNode.data == nodeValue:
            return "Success! Node Found."

        if currentNode.leftChild is not None:
            customQueue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            customQueue.append(currentNode.rightChild)

    return "Node Not Found."


# -----------------------------------------------------
# Insert Node in Binary Tree
# Insert at first vacant place using Level Order Traversal
# Time Complexity : O(n)
# Space Complexity : O(n)
# -----------------------------------------------------

def insertNodeBt(rootNode, newNode):
    if rootNode is None:
        rootNode = newNode
        return "Successfully Inserted"

    customQueue = deque()
    customQueue.append(rootNode)

    while customQueue:
        currentNode = customQueue.popleft()

        if currentNode.leftChild is not None:
            customQueue.append(currentNode.leftChild)
        else:
            currentNode.leftChild = newNode
            return "Successfully Inserted"

        if currentNode.rightChild is not None:
            customQueue.append(currentNode.rightChild)
        else:
            currentNode.rightChild = newNode
            return "Successfully Inserted"


# -----------------------------------------------------
# Get Deepest Node
# Last node in Level Order Traversal
# Time Complexity : O(n)
# Space Complexity : O(n)
# -----------------------------------------------------

def getDeepestNode(rootNode):
    if rootNode is None:
        return None

    customQueue = deque()
    customQueue.append(rootNode)

    currentNode = None

    while customQueue:
        currentNode = customQueue.popleft()

        if currentNode.leftChild is not None:
            customQueue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            customQueue.append(currentNode.rightChild)

    return currentNode


# -----------------------------------------------------
# Delete Deepest Node
# Time Complexity : O(n)
# Space Complexity : O(n)
# -----------------------------------------------------

def deleteDeepestNode(rootNode, deepestNode):
    if rootNode is None:
        return

    customQueue = deque()
    customQueue.append(rootNode)

    while customQueue:
        currentNode = customQueue.popleft()

        # If root itself is deepest node
        if currentNode is deepestNode:
            currentNode = None
            return

        # Check right child
        if currentNode.rightChild is not None:
            if currentNode.rightChild is deepestNode:
                currentNode.rightChild = None
                return
            else:
                customQueue.append(currentNode.rightChild)

        # Check left child
        if currentNode.leftChild is not None:
            if currentNode.leftChild is deepestNode:
                currentNode.leftChild = None
                return
            else:
                customQueue.append(currentNode.leftChild)


# -----------------------------------------------------
# Delete Node From Binary Tree
#
# Logic:
# 1. Find node to delete
# 2. Find deepest node
# 3. Replace target node data with deepest node data
# 4. Delete deepest node
#
# Time Complexity : O(n)
# Space Complexity : O(n)
# -----------------------------------------------------

def deleteNodeBT(rootNode, nodeValue):
    if rootNode is None:
        return "The Binary Tree does not exist."

    customQueue = deque()
    customQueue.append(rootNode)

    nodeToDelete = None

    while customQueue:
        currentNode = customQueue.popleft()

        if currentNode.data == nodeValue:
            nodeToDelete = currentNode

        if currentNode.leftChild is not None:
            customQueue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            customQueue.append(currentNode.rightChild)

    if nodeToDelete is None:
        return "Node Not Found."

    deepestNode = getDeepestNode(rootNode)

    nodeToDelete.data = deepestNode.data

    deleteDeepestNode(rootNode, deepestNode)

    return "Node Deleted Successfully."


# -----------------------------------------------------
# Delete Entire Binary Tree
# Time Complexity : O(1)
# Space Complexity : O(1)
# -----------------------------------------------------

def deleteEntireBT(rootNode):
    if rootNode is None:
        return "The Binary Tree does not exist."

    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

    return "Binary Tree Deleted Successfully."


# -----------------------------------------------------
# Driver Code
# -----------------------------------------------------

print("Preorder Traversal:")
preOrderTraversal(NewBT)

print("\nInorder Traversal:")
inOrderTraversal(NewBT)

print("\nPostorder Traversal:")
postOrderTraversal(NewBT)

print("\nLevel Order Traversal:")
levelOrderTraversal(NewBT)


print("\nSearch Result:")
print(searchBT(NewBT, "Cold"))


print("\nAfter Inserting Guns:")
newNode = TreeNode("Guns")
print(insertNodeBt(NewBT, newNode))
levelOrderTraversal(NewBT)


print("\nDeepest Node:")
deepestNode = getDeepestNode(NewBT)
print(deepestNode.data)


print("\nAfter Deleting Cold:")
print(deleteNodeBT(NewBT, "Cold"))
levelOrderTraversal(NewBT)


print("\nDeleting Entire Binary Tree:")
print(deleteEntireBT(NewBT))

print("\nLevel Order Traversal After Deleting Entire Tree:")
levelOrderTraversal(NewBT)