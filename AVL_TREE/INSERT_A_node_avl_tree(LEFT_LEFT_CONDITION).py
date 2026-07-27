from collections import deque


# ============================================================
# AVL TREE NODE
# ============================================================
class AVLNode:
    def __init__(self, data):
        self.data = data

        # Left and right children
        self.leftChild = None
        self.rightChild = None

        # Height of a newly created node is 1
        self.height = 1


# ============================================================
# PREORDER TRAVERSAL
# Root -> Left -> Right
# ============================================================
def preOrderTraversal(rootNode):
    if rootNode is None:
        return

    print(rootNode.data, end=" ")

    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# ============================================================
# INORDER TRAVERSAL
# Left -> Root -> Right
#
# In an AVL tree, inorder traversal prints values
# in sorted order.
# ============================================================
def inOrderTraversal(rootNode):
    if rootNode is None:
        return

    inOrderTraversal(rootNode.leftChild)

    print(rootNode.data, end=" ")

    inOrderTraversal(rootNode.rightChild)


# ============================================================
# POSTORDER TRAVERSAL
# Left -> Right -> Root
# ============================================================
def postOrderTraversal(rootNode):
    if rootNode is None:
        return

    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)

    print(rootNode.data, end=" ")


# ============================================================
# LEVEL ORDER TRAVERSAL
# BFS traversal using a queue
# ============================================================
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return

    queue = deque([rootNode])

    while queue:
        currentNode = queue.popleft()

        print(currentNode.data, end=" ")

        if currentNode.leftChild is not None:
            queue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            queue.append(currentNode.rightChild)


# ============================================================
# HELPER FUNCTION TO GET HEIGHT
# ============================================================
def getHeight(rootNode):
    if rootNode is None:
        return 0

    return rootNode.height


# ============================================================
# HELPER FUNCTION TO GET BALANCE FACTOR
#
# Balance factor =
# height of left subtree - height of right subtree
#
# Balanced AVL node:
# -1, 0, or 1
# ============================================================
def getBalance(rootNode):
    if rootNode is None:
        return 0

    return (
        getHeight(rootNode.leftChild)
        - getHeight(rootNode.rightChild)
    )


# ============================================================
# RIGHT ROTATION
#
# Used mainly for Left-Left condition
#
# Before:
#
#          y
#         /
#        x
#         \
#          T2
#
# After:
#
#          x
#           \
#            y
#           /
#          T2
# ============================================================
def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild

    # Save the subtree that will be transferred
    transferredSubtree = newRoot.rightChild

    # Perform rotation
    newRoot.rightChild = disbalancedNode
    disbalancedNode.leftChild = transferredSubtree

    # Update height of old root first
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild),
        getHeight(disbalancedNode.rightChild)
    )

    # Update height of new root
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild),
        getHeight(newRoot.rightChild)
    )

    return newRoot


# ============================================================
# LEFT ROTATION
#
# Used mainly for Right-Right condition
#
# Before:
#
#      y
#       \
#        x
#       /
#      T2
#
# After:
#
#        x
#       /
#      y
#       \
#        T2
# ============================================================
def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild

    # Save the subtree that will be transferred
    transferredSubtree = newRoot.leftChild

    # Perform rotation
    newRoot.leftChild = disbalancedNode
    disbalancedNode.rightChild = transferredSubtree

    # Update height of old root first
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild),
        getHeight(disbalancedNode.rightChild)
    )

    # Update height of new root
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild),
        getHeight(newRoot.rightChild)
    )

    return newRoot


# ============================================================
# AVL INSERTION
#
# Four imbalance cases:
#
# 1. Left-Left   -> Right Rotation
# 2. Left-Right  -> Left Rotation + Right Rotation
# 3. Right-Right -> Left Rotation
# 4. Right-Left  -> Right Rotation + Left Rotation
# ============================================================
def insertNode(rootNode, nodeValue):

    # Normal BST insertion
    if rootNode is None:
        return AVLNode(nodeValue)

    if nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(
            rootNode.leftChild,
            nodeValue
        )

    elif nodeValue > rootNode.data:
        rootNode.rightChild = insertNode(
            rootNode.rightChild,
            nodeValue
        )

    else:
        # Duplicate values are not inserted
        return rootNode

    # Update height of current node
    rootNode.height = 1 + max(
        getHeight(rootNode.leftChild),
        getHeight(rootNode.rightChild)
    )

    # Calculate balance factor
    balance = getBalance(rootNode)

    # --------------------------------------------------------
    # Case 1: Left-Left condition
    #
    # New value was inserted in the left subtree
    # of the left child.
    # --------------------------------------------------------
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)

    # --------------------------------------------------------
    # Case 2: Left-Right condition
    #
    # First rotate left child toward the left,
    # then rotate current root toward the right.
    # --------------------------------------------------------
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)

    # --------------------------------------------------------
    # Case 3: Right-Right condition
    #
    # New value was inserted in the right subtree
    # of the right child.
    # --------------------------------------------------------
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)

    # --------------------------------------------------------
    # Case 4: Right-Left condition
    #
    # First rotate right child toward the right,
    # then rotate current root toward the left.
    # --------------------------------------------------------
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)

    # If the node is already balanced
    return rootNode


# ============================================================
# DRIVER CODE
# ============================================================
root = None

values = [30, 20, 40, 10, 25, 50, 5]

for value in values:
    root = insertNode(root, value)


print("Preorder Traversal:")
preOrderTraversal(root)

print("\n\nInorder Traversal:")
inOrderTraversal(root)

print("\n\nPostorder Traversal:")
postOrderTraversal(root)

print("\n\nLevel Order Traversal:")
levelOrderTraversal(root)