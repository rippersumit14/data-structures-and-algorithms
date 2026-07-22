"""
------------------------------------------------------------
Binary Search Tree: Insertion and Traversals
------------------------------------------------------------

DFS Traversals:
1. Preorder  -> Root, Left, Right
2. Inorder   -> Left, Root, Right
3. Postorder -> Left, Right, Root

BFS Traversal:
1. Level-order traversal
------------------------------------------------------------
"""

from collections import deque


# ------------------------------------------------------------
# BST Node
# ------------------------------------------------------------

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# ------------------------------------------------------------
# Insert a Node into the BST
# ------------------------------------------------------------

def insert_node(rootNode, value):

    # Edge case: the root node contains no value
    if rootNode.data is None:
        rootNode.data = value
        return

    # Smaller or equal values go to the left subtree
    if value <= rootNode.data:

        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(value)
        else:
            insert_node(rootNode.leftChild, value)

    # Greater values go to the right subtree
    else:

        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insert_node(rootNode.rightChild, value)


"""
Insertion Complexity:

Time Complexity:
- Balanced BST: O(log n)
- Skewed BST: O(n)
- General form: O(h), where h is the tree height

Space Complexity:
- Balanced BST: O(log n)
- Skewed BST: O(n)
- General form: O(h)

The space is used by the recursive call stack.
"""


# ------------------------------------------------------------
# Preorder Traversal
# Root -> Left -> Right
# ------------------------------------------------------------

def preorder_traversal(rootNode):

    # Base case
    if rootNode is None:
        return

    print(rootNode.data, end=" ")

    preorder_traversal(rootNode.leftChild)
    preorder_traversal(rootNode.rightChild)


"""
Preorder Complexity:

Time Complexity: O(n)
Every node is visited exactly once.

Space Complexity:
- Balanced tree: O(log n)
- Skewed tree: O(n)
- General form: O(h)

The space is used by the recursive call stack.
"""


# ------------------------------------------------------------
# Inorder Traversal
# Left -> Root -> Right
# ------------------------------------------------------------

def inorder_traversal(rootNode):

    # Base case
    if rootNode is None:
        return

    inorder_traversal(rootNode.leftChild)

    print(rootNode.data, end=" ")

    inorder_traversal(rootNode.rightChild)


"""
Inorder Complexity:

Time Complexity: O(n)
Every node is visited exactly once.

Space Complexity:
- Balanced tree: O(log n)
- Skewed tree: O(n)
- General form: O(h)

For a BST, inorder traversal prints the values
in sorted ascending order.
"""


# ------------------------------------------------------------
# Postorder Traversal
# Left -> Right -> Root
# ------------------------------------------------------------

def postorder_traversal(rootNode):

    # Base case
    if rootNode is None:
        return

    postorder_traversal(rootNode.leftChild)
    postorder_traversal(rootNode.rightChild)

    print(rootNode.data, end=" ")


"""
Postorder Complexity:

Time Complexity: O(n)
Every node is visited exactly once.

Space Complexity:
- Balanced tree: O(log n)
- Skewed tree: O(n)
- General form: O(h)

The space is used by the recursive call stack.
"""


# ------------------------------------------------------------
# Level-order Traversal
# BFS: Visit nodes level by level
# ------------------------------------------------------------

def level_order_traversal(rootNode):

    if rootNode is None or rootNode.data is None:
        return

    queue = deque()
    queue.append(rootNode)

    while queue:

        currentNode = queue.popleft()

        print(currentNode.data, end=" ")

        if currentNode.leftChild is not None:
            queue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            queue.append(currentNode.rightChild)


"""
Level-order Complexity:

Time Complexity: O(n)
Every node is added to and removed from the queue once.

Space Complexity: O(w)

Here, w is the maximum width of the tree.

Worst-case Space Complexity: O(n)
because one level may contain approximately half of all nodes.
"""


# ------------------------------------------------------------
# Creating the BST
# ------------------------------------------------------------

newBST = BSTNode(None)

insert_node(newBST, 70)
insert_node(newBST, 50)
insert_node(newBST, 90)
insert_node(newBST, 30)
insert_node(newBST, 60)
insert_node(newBST, 76)
insert_node(newBST, 100)


# ------------------------------------------------------------
# Displaying All Traversals
# ------------------------------------------------------------

print("Preorder Traversal:")
preorder_traversal(newBST)
print()


print("Inorder Traversal:")
inorder_traversal(newBST)
print()


print("Postorder Traversal:")
postorder_traversal(newBST)
print()


print("Level-order Traversal:")
level_order_traversal(newBST)
print()