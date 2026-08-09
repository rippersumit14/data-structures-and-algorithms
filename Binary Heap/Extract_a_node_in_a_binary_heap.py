# -----------------------------------------------------
# Binary Heap
# -----------------------------------------------------

# A Binary Heap is a Complete Binary Tree.

# It is generally implemented using an array
# instead of linked tree nodes.

# Binary Heap is mainly used to implement a Priority Queue.

# There are two types of Binary Heap:
# 1. Min Heap -> Parent Node <= Child Nodes
# 2. Max Heap -> Parent Node >= Child Nodes

# Complete Binary Tree:
# Every level is completely filled except possibly the last level.
# The last level is filled from left to right.

# Heap Property:
# Every parent node follows the Min Heap or Max Heap rule.

# A Binary Heap does not maintain the complete array
# in sorted order.
# It only guarantees the heap property.

# Root Node:
# Min Heap -> Smallest element is at the root.
# Max Heap -> Largest element is at the root.

# This implementation uses 1-based indexing.

# Array Index Formulas for 1-based indexing:
# Left Child  = 2 * i
# Right Child = 2 * i + 1
# Parent      = i // 2

# Common Operations:
# Insert
# Peek
# Extract Root
# Heapify Up
# Heapify Down
# Build Heap


# -----------------------------------------------------
# Binary Heap Class
# -----------------------------------------------------

class Heap:
    def __init__(self, size):

        # We use size + 1 because index 0 is unused.
        self.customList = [None] * (size + 1)

        # Number of actual elements currently in the heap.
        self.heapSize = 0

        # Total length of the internal array.
        self.maxSize = size + 1


# -----------------------------------------------------
# Peek the Root Node
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------------------

def peekOfHeap(rootNode):

    # Heap does not exist or is empty.
    if rootNode is None or rootNode.heapSize == 0:
        return None

    # Root element is stored at index 1.
    return rootNode.customList[1]


# -----------------------------------------------------
# Return the Number of Elements in the Heap
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------------------

def sizeOfBinaryHeap(rootNode):

    if rootNode is None:
        return 0

    return rootNode.heapSize


# -----------------------------------------------------
# Heapify Up
#
# Used after insertion.
# It compares the inserted node with its parent
# and moves it upward until the heap property is restored.
#
# Time Complexity: O(log n)
# Space Complexity: O(log n) because of recursion stack
# -----------------------------------------------------

def heapifyUp(rootNode, index, heapType):

    # Root node has no parent.
    if index <= 1:
        return

    parentIndex = index // 2

    if heapType == "Min":

        # Swap when the child is smaller than the parent.
        if (
            rootNode.customList[index]
            < rootNode.customList[parentIndex]
        ):
            rootNode.customList[index], rootNode.customList[parentIndex] = (
                rootNode.customList[parentIndex],
                rootNode.customList[index]
            )

            # Continue checking upward.
            heapifyUp(rootNode, parentIndex, heapType)

    elif heapType == "Max":

        # Swap when the child is greater than the parent.
        if (
            rootNode.customList[index]
            > rootNode.customList[parentIndex]
        ):
            rootNode.customList[index], rootNode.customList[parentIndex] = (
                rootNode.customList[parentIndex],
                rootNode.customList[index]
            )

            # Continue checking upward.
            heapifyUp(rootNode, parentIndex, heapType)

    else:
        raise ValueError("heapType must be either 'Min' or 'Max'.")


# -----------------------------------------------------
# Level Order Traversal
#
# Since the heap is stored in an array,
# traversing the array from index 1 gives level order.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------

def levelOrderTraversal(rootNode):

    if rootNode is None or rootNode.heapSize == 0:
        print("The binary heap is empty.")
        return

    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i], end=" ")

    print()


# -----------------------------------------------------
# Insert a Node into the Binary Heap
#
# Steps:
# 1. Insert the value into the next empty position.
# 2. Increase the heap size.
# 3. Use heapify-up to restore the heap property.
#
# Time Complexity: O(log n)
# Space Complexity: O(log n) because heapify uses recursion
# -----------------------------------------------------

def insertNode(rootNode, nodeValue, heapType):

    if rootNode is None:
        return "The binary heap does not exist."

    if heapType not in ("Min", "Max"):
        return "Heap type must be either 'Min' or 'Max'."

    # Check whether the heap is full.
    if rootNode.heapSize + 1 >= rootNode.maxSize:
        return "The binary heap is full."

    # Insert at the next available position.
    rootNode.heapSize += 1
    rootNode.customList[rootNode.heapSize] = nodeValue

    # Restore heap property.
    heapifyUp(rootNode, rootNode.heapSize, heapType)

    return "The value has been successfully inserted."

#Extracting a node in binary heap
# -----------------------------------------------------
# Heapify Down
#
# Used after extracting/deleting the root.
# It compares the current node with its children
# and moves it downward until the heap property is restored.
#
# Time Complexity: O(log n)
# Space Complexity: O(log n) because of recursion
# -----------------------------------------------------

def heapifyDown(rootNode, index, heapType):

    leftIndex = index * 2
    rightIndex = index * 2 + 1

    # If there is no left child,
    # the current node is already a leaf node.
    if leftIndex > rootNode.heapSize:
        return

    if heapType == "Min":

        # Assume the left child is the smaller child.
        smallerChildIndex = leftIndex

        # Check whether the right child exists
        # and is smaller than the left child.
        if (
            rightIndex <= rootNode.heapSize
            and rootNode.customList[rightIndex]
            < rootNode.customList[leftIndex]
        ):
            smallerChildIndex = rightIndex

        # Swap only when the current node is greater
        # than the smaller child.
        if (
            rootNode.customList[index]
            > rootNode.customList[smallerChildIndex]
        ):
            rootNode.customList[index], rootNode.customList[smallerChildIndex] = (
                rootNode.customList[smallerChildIndex],
                rootNode.customList[index]
            )

            heapifyDown(rootNode, smallerChildIndex, heapType)

    elif heapType == "Max":

        # Assume the left child is the larger child.
        largerChildIndex = leftIndex

        # Check whether the right child exists
        # and is larger than the left child.
        if (
            rightIndex <= rootNode.heapSize
            and rootNode.customList[rightIndex]
            > rootNode.customList[leftIndex]
        ):
            largerChildIndex = rightIndex

        # Swap only when the current node is smaller
        # than the larger child.
        if (
            rootNode.customList[index]
            < rootNode.customList[largerChildIndex]
        ):
            rootNode.customList[index], rootNode.customList[largerChildIndex] = (
                rootNode.customList[largerChildIndex],
                rootNode.customList[index]
            )

            heapifyDown(rootNode, largerChildIndex, heapType)

    else:
        raise ValueError("heapType must be either 'Min' or 'Max'.")


# -----------------------------------------------------
# Extract Root Node from Binary Heap
#
# Min Heap -> Extracts the minimum element.
# Max Heap -> Extracts the maximum element.
#
# Time Complexity: O(log n)
# Space Complexity: O(log n) because heapifyDown is recursive
# -----------------------------------------------------

def extractNode(rootNode, heapType):

    if rootNode is None:
        return "The binary heap does not exist."

    if rootNode.heapSize == 0:
        return "The binary heap is empty."

    if heapType not in ("Min", "Max"):
        return "Heap type must be either 'Min' or 'Max'."

    # Save the root value before removing it.
    extractedValue = rootNode.customList[1]

    # Move the last element to the root position.
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]

    # Remove the old last element.
    rootNode.customList[rootNode.heapSize] = None

    # Reduce the heap size.
    rootNode.heapSize -= 1

    # Restore the heap property.
    if rootNode.heapSize > 0:
        heapifyDown(rootNode, 1, heapType)

    return extractedValue



# -----------------------------------------------------
# Driver Code: Max Heap
# -----------------------------------------------------

print("Creating Max Heap:")

newBinaryHeap = Heap(5)

print(insertNode(newBinaryHeap, 4, "Max"))
print(insertNode(newBinaryHeap, 5, "Max"))
print(insertNode(newBinaryHeap, 2, "Max"))
print(insertNode(newBinaryHeap, 1, "Max"))
print(insertNode(newBinaryHeap, 8, "Max"))

print("\nMax Heap Level Order Traversal:")
levelOrderTraversal(newBinaryHeap)

print("Root of Max Heap:", peekOfHeap(newBinaryHeap))
print("Size of Max Heap:", sizeOfBinaryHeap(newBinaryHeap))


# -----------------------------------------------------
# Driver Code: Min Heap
# -----------------------------------------------------

print("\nCreating Min Heap:")

minBinaryHeap = Heap(5)

print(insertNode(minBinaryHeap, 4, "Min"))
print(insertNode(minBinaryHeap, 5, "Min"))
print(insertNode(minBinaryHeap, 2, "Min"))
print(insertNode(minBinaryHeap, 1, "Min"))
print(insertNode(minBinaryHeap, 8, "Min"))

print("\nMin Heap Level Order Traversal:")
levelOrderTraversal(minBinaryHeap)

print("Root of Min Heap:", peekOfHeap(minBinaryHeap))
print("Size of Min Heap:", sizeOfBinaryHeap(minBinaryHeap))